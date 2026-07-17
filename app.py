import json

import plotly.express as px
from plotly.utils import PlotlyJSONEncoder
from flask import Flask, render_template, request, session, redirect, url_for

from services.recommender_service import (
    get_popular_products,
    search_products,
    get_product_recommendations,
    get_customer_recommendations,
    get_customer_purchase_history,
    get_dashboard_data,
    get_product_catalog,
    get_product_by_stock_code,
    get_shop_categories,
    get_cart_products,
    get_product_page_recommendations,
    get_ml_product_recommendation_sections,
    get_customer_segment
)

app = Flask(__name__)
app.secret_key = "oviu-development-secret-key"


def create_chart_json(fig):
    return json.dumps(fig, cls=PlotlyJSONEncoder)


def create_dashboard_charts(data):
    charts = {}

    if not data:
        return charts

    top_products = data.get("top_products", [])
    top_countries = data.get("top_countries", [])
    monthly_revenue = data.get("monthly_revenue", [])

    if top_products:
        fig_products = px.bar(
            top_products[:10],
            x="total_quantity",
            y="Description",
            orientation="h",
            title="Top 10 Products by Quantity Sold",
            labels={
                "total_quantity": "Total Quantity Sold",
                "Description": "Product"
            }
        )

        fig_products.update_layout(
            yaxis={"categoryorder": "total ascending"},
            height=520,
            margin=dict(l=30, r=30, t=70, b=30)
        )

        charts["top_products_chart"] = create_chart_json(fig_products)

    if top_countries:
        fig_countries = px.bar(
            top_countries,
            x="Country",
            y="total_revenue",
            title="Top Countries by Revenue",
            labels={
                "Country": "Country",
                "total_revenue": "Total Revenue (£)"
            }
        )

        fig_countries.update_layout(
            height=460,
            margin=dict(l=30, r=30, t=70, b=30)
        )

        charts["top_countries_chart"] = create_chart_json(fig_countries)

    if monthly_revenue:
        fig_monthly = px.line(
            monthly_revenue,
            x="month",
            y="total_revenue",
            markers=True,
            title="Monthly Revenue Trend",
            labels={
                "month": "Month",
                "total_revenue": "Total Revenue (£)"
            }
        )

        fig_monthly.update_layout(
            height=460,
            margin=dict(l=30, r=30, t=70, b=30)
        )

        charts["monthly_revenue_chart"] = create_chart_json(fig_monthly)

    return charts


@app.route("/")
def home():
    popular_products = get_popular_products(limit=6)

    return render_template(
        "index.html",
        popular_products=popular_products
    )


@app.route("/shop")
def shop():
    search_text = request.args.get("search", "").strip()
    category = request.args.get("category", "").strip()

    products = get_product_catalog(
        limit=60,
        search_text=search_text,
        category=category
    )

    categories = get_shop_categories()

    return render_template(
        "shop.html",
        products=products,
        categories=categories,
        search_text=search_text,
        selected_category=category
    )


@app.route("/product/<path:stock_code>")
def product_detail(stock_code):
    product = get_product_by_stock_code(stock_code)

    if not product:
        return redirect(url_for("shop"))

    ml_recommendation_sections = get_ml_product_recommendation_sections(
        product,
        limit=4
    )

    recommended_products = get_product_page_recommendations(
        product,
        limit=6
    )

    return render_template(
        "product_detail.html",
        product=product,
        recommended_products=recommended_products,
        ml_recommendation_sections=ml_recommendation_sections
    )


@app.route("/add-to-cart/<path:stock_code>", methods=["POST"])
def add_to_cart(stock_code):
    cart = session.get("cart", {})
    stock_code = str(stock_code)

    cart[stock_code] = cart.get(stock_code, 0) + 1

    session["cart"] = cart
    session.modified = True

    return redirect(request.referrer or url_for("shop"))


@app.route("/remove-from-cart/<path:stock_code>", methods=["POST"])
def remove_from_cart(stock_code):
    cart = session.get("cart", {})
    stock_code = str(stock_code)

    if stock_code in cart:
        cart[stock_code] -= 1

        if cart[stock_code] <= 0:
            del cart[stock_code]

    session["cart"] = cart
    session.modified = True

    return redirect(url_for("cart"))


@app.route("/clear-cart", methods=["POST"])
def clear_cart():
    session["cart"] = {}
    session.modified = True

    return redirect(url_for("cart"))


@app.route("/cart")
def cart():
    cart_data = session.get("cart", {})
    cart_items, cart_total = get_cart_products(cart_data)

    recommended_products = get_product_catalog(limit=6)

    return render_template(
        "cart.html",
        cart_items=cart_items,
        cart_total=cart_total,
        recommended_products=recommended_products
    )


@app.route("/recommendations", methods=["GET", "POST"])
def recommendations():
    product_name = ""
    customer_id = ""
    recommendation_type = "product"

    recommended_products = []
    searched_products = []
    purchased_products = []
    customer_segment = None

    if request.method == "POST":
        recommendation_type = request.form.get("recommendation_type", "product")
        product_name = request.form.get("product_name", "").strip()
        customer_id = request.form.get("customer_id", "").strip()

        if recommendation_type == "product":
            recommended_products = get_product_recommendations(
                product_name,
                limit=10
            )

            searched_products = search_products(
                product_name,
                limit=5
            )

        elif recommendation_type == "customer":
            recommended_products = get_customer_recommendations(
                customer_id,
                limit=10
            )

            purchased_products = get_customer_purchase_history(
                customer_id,
                limit=10
            )

            customer_segment = get_customer_segment(customer_id)

    popular_products = get_popular_products(limit=10)

    return render_template(
        "recommendations.html",
        recommendation_type=recommendation_type,
        product_name=product_name,
        customer_id=customer_id,
        searched_products=searched_products,
        purchased_products=purchased_products,
        recommended_products=recommended_products,
        popular_products=popular_products,
        customer_segment=customer_segment
    )


@app.route("/dashboard")
def dashboard():
    data = get_dashboard_data()
    charts = create_dashboard_charts(data)

    return render_template(
        "dashboard.html",
        data=data,
        charts=charts
    )


if __name__ == "__main__":
    app.run(debug=True)