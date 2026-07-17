import json
from pathlib import Path


MODEL_DIR = Path("models")


def load_json_file(filename, default_value):
    file_path = MODEL_DIR / filename

    if not file_path.exists():
        return default_value

    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


popular_products = load_json_file("popular_products.json", [])
item_recommendations = load_json_file("item_recommendations.json", {})
customer_products = load_json_file("customer_products.json", {})
product_index = load_json_file("product_index.json", [])
dashboard_data = load_json_file("dashboard_data.json", {})

product_catalog = load_json_file("product_catalog.json", [])
product_lookup = load_json_file("product_lookup.json", {})

content_based_recommendations = load_json_file("content_based_recommendations.json", {})
collaborative_recommendations = load_json_file("collaborative_recommendations.json", {})
matrix_factorization_recommendations = load_json_file("matrix_factorization_recommendations.json", {})
market_basket_recommendations = load_json_file("market_basket_recommendations.json", {})
customer_segments_data = load_json_file("customer_segments.json", {})


def get_popular_products(limit=10):
    return popular_products[:limit]


def search_products(search_text, limit=10):
    if not search_text:
        return []

    search_text = search_text.lower().strip()
    results = []

    for product in product_index:
        product_name = product.get("Description", "")

        if search_text in product_name.lower():
            results.append(product)

        if len(results) >= limit:
            break

    return results


def get_product_catalog(limit=60, search_text="", category=""):
    products = product_catalog

    if search_text:
        search_text = search_text.lower().strip()
        products = [
            product for product in products
            if search_text in product.get("name", "").lower()
            or search_text in product.get("description", "").lower()
            or search_text in product.get("stock_code", "").lower()
        ]

    if category:
        products = [
            product for product in products
            if product.get("category", "").lower() == category.lower()
        ]

    return products[:limit]


def get_product_by_stock_code(stock_code):
    if not stock_code:
        return None

    return product_lookup.get(str(stock_code))


def get_shop_categories():
    categories = sorted({
        product.get("category", "General")
        for product in product_catalog
    })

    return categories


def find_catalog_product_by_name(product_name):
    if not product_name:
        return None

    product_name_lower = product_name.lower().strip()

    for product in product_catalog:
        if product.get("description", "").lower().strip() == product_name_lower:
            return product

    for product in product_catalog:
        if product_name_lower in product.get("description", "").lower():
            return product

    return None


def convert_ml_items_to_catalog_items(items, limit=6):
    catalog_items = []
    seen_stock_codes = set()

    for item in items:
        stock_code = str(item.get("stock_code", "")).strip()
        product = None

        if stock_code:
            product = get_product_by_stock_code(stock_code)

        if not product:
            product = find_catalog_product_by_name(item.get("product", ""))

        if not product:
            continue

        if product["stock_code"] in seen_stock_codes:
            continue

        product_copy = product.copy()
        product_copy["ml_score"] = item.get("score", 0)
        product_copy["ml_method"] = item.get("method", "ML Recommendation")

        catalog_items.append(product_copy)
        seen_stock_codes.add(product["stock_code"])

        if len(catalog_items) >= limit:
            break

    return catalog_items


def get_product_recommendations(product_name, limit=10):
    if not product_name:
        return get_popular_products(limit)

    product_name = product_name.strip()

    if product_name in market_basket_recommendations:
        return market_basket_recommendations[product_name][:limit]

    if product_name in item_recommendations:
        return item_recommendations[product_name][:limit]

    matched_products = search_products(product_name, limit=1)

    if matched_products:
        matched_name = matched_products[0].get("Description", "")

        if matched_name in market_basket_recommendations:
            return market_basket_recommendations[matched_name][:limit]

        if matched_name in item_recommendations:
            return item_recommendations[matched_name][:limit]

    popular = get_popular_products(limit)

    return [
        {
            "product": item.get("Description", "Unknown Product"),
            "score": item.get("total_quantity", 0),
            "method": "Popularity-Based Recommendation"
        }
        for item in popular
    ]


def get_ml_product_recommendation_sections(product, limit=6):
    if not product:
        return {}

    description = product.get("description", "")

    sections = {
        "Content-Based Filtering": convert_ml_items_to_catalog_items(
            content_based_recommendations.get(description, []),
            limit=limit
        ),
        "Collaborative Filtering": convert_ml_items_to_catalog_items(
            collaborative_recommendations.get(description, []),
            limit=limit
        ),
        "Matrix Factorization": convert_ml_items_to_catalog_items(
            matrix_factorization_recommendations.get(description, []),
            limit=limit
        ),
        "Market Basket Analysis": convert_ml_items_to_catalog_items(
            market_basket_recommendations.get(description, []),
            limit=limit
        )
    }

    for section_name, products in sections.items():
        if not products:
            sections[section_name] = get_product_catalog(limit=limit)

    return sections


def get_customer_purchase_history(customer_id, limit=10):
    if not customer_id:
        return []

    customer_id = str(customer_id).strip()
    products = customer_products.get(customer_id, [])

    return products[:limit]


def get_customer_segment(customer_id):
    if not customer_id:
        return None

    customer_id = str(customer_id).strip()

    customer_segments = customer_segments_data.get("customer_segments", {})

    return customer_segments.get(customer_id)


def get_customer_recommendations(customer_id, limit=10):
    purchased_products = get_customer_purchase_history(customer_id, limit=20)

    if not purchased_products:
        return get_popular_products(limit)

    recommendations = []
    seen = set(purchased_products)

    for product in purchased_products:
        related_items = market_basket_recommendations.get(product, [])

        if not related_items:
            related_items = collaborative_recommendations.get(product, [])

        for item in related_items:
            item_name = item.get("product")

            if item_name and item_name not in seen:
                recommendations.append(item)
                seen.add(item_name)

            if len(recommendations) >= limit:
                return recommendations

    return recommendations[:limit]


def get_dashboard_data():
    return dashboard_data


def get_cart_products(cart):
    cart_items = []
    cart_total = 0

    for stock_code, quantity in cart.items():
        product = get_product_by_stock_code(stock_code)

        if not product:
            continue

        item_total = product.get("price", 0) * quantity
        cart_total += item_total

        cart_items.append({
            "product": product,
            "quantity": quantity,
            "item_total": round(item_total, 2)
        })

    return cart_items, round(cart_total, 2)


def get_product_page_recommendations(product, limit=6):
    sections = get_ml_product_recommendation_sections(product, limit=limit)

    if sections:
        first_section = list(sections.values())[0]
        return first_section[:limit]

    return get_product_catalog(limit=limit)