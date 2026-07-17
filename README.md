# OVIU Hybrid Product Recommendation System

OVIU is an e-commerce style product purchasing website integrated with a hybrid machine learning recommendation system. The project uses an online retail transaction dataset to analyze customer purchase behavior, generate product recommendations, simulate shopping cart functionality, and display business insights through an analytics dashboard.

The main goal of this project is to demonstrate how machine learning techniques can be connected with a real product purchasing website to improve product discovery, customer personalization, and business decision-making.

---

## Project Overview

This project is not only a data analysis dashboard. It is a complete Flask web application where users can browse products, view product details, add products to cart, and receive product recommendations generated from machine learning models.

The system is designed for an OVIU-style online product business where customers can purchase creative, customized, or retail products and receive smart recommendations.

---

## Main Features

- E-commerce style home page
- Product shop page
- Product search and category filtering
- Product detail page
- Add-to-cart simulation
- Cart page with total price calculation
- Product-based recommendations
- Customer-based recommendations
- Customer segmentation
- Analytics dashboard
- ML-powered recommendation sections on product pages

---

## Machine Learning Techniques Used

### 1. Popularity-Based Recommendation

This is the baseline recommendation method. It recommends products based on total quantity sold, number of orders, and total revenue.

### 2. Market Basket Analysis

This technique finds products that are frequently purchased together in the same invoice or shopping basket.

Example:

```text
Customers who bought Product A also bought Product B
```

### 3. Content-Based Filtering

This method recommends similar products based on product descriptions.

Techniques used:

- TF-IDF Vectorization
- Cosine Similarity

### 4. Item-Based Collaborative Filtering

This method recommends products based on customer-product purchase behavior.

Techniques used:

- Customer-product interaction matrix
- Cosine similarity

### 5. Matrix Factorization

This method learns hidden relationships between customers and products.

Technique used:

- TruncatedSVD

### 6. Customer Segmentation

This method groups customers based on purchase behavior.

Technique used:

- K-Means Clustering

Customer features used:

- Total spending
- Total orders
- Total quantity purchased
- Unique products purchased
- Average order value

---

## Dataset Information

The project uses an online retail transaction dataset.

Main dataset columns:

| Column | Description |
|---|---|
| Invoice | Transaction or invoice number |
| StockCode | Product stock code |
| Description | Product name or description |
| Quantity | Number of items purchased |
| InvoiceDate | Date and time of purchase |
| Price | Product unit price |
| Customer ID | Customer identifier |
| Country | Customer country |

The dataset does not include product image URLs. Because of this limitation, the website uses category-based placeholder visuals and icons for product cards.

The machine learning models do not require product images because they use transaction history, product descriptions, customer IDs, quantity, invoice data, and price.

---

## Website Pages

### Home Page

The home page introduces the OVIU hybrid recommendation system and shows top products from the dataset.

### Shop Page

The shop page displays product cards generated from the cleaned retail dataset. Users can search products, filter by category, view product details, and add products to cart.

### Product Detail Page

The product detail page displays product information and ML-powered recommendations.

Recommendation sections include:

- Content-Based Filtering
- Collaborative Filtering
- Matrix Factorization
- Market Basket Analysis

### Cart Page

The cart page simulates a purchasing flow. Users can add products, remove products, clear the cart, and view total cart value.

### Recommendations Page

The recommendations page allows users to test product-based and customer-based recommendations. For customer-based recommendations, the system also displays the customer segment generated using K-Means clustering.

### Dashboard Page

The dashboard shows dataset insights such as total transactions, total products, total customers, total revenue, top products, top countries, and monthly revenue trends.

---

## System Architecture

```text
Online Retail Dataset
        ↓
Data Cleaning and Preprocessing
        ↓
Feature Engineering
        ↓
Machine Learning Models
        ├── Popularity-Based Recommendation
        ├── Market Basket Analysis
        ├── TF-IDF Content-Based Filtering
        ├── Item-Based Collaborative Filtering
        ├── Matrix Factorization with TruncatedSVD
        └── K-Means Customer Segmentation
        ↓
Saved JSON Model Files
        ↓
Flask Service Layer
        ↓
E-Commerce Website
        ├── Home Page
        ├── Shop Page
        ├── Product Detail Page
        ├── Cart Page
        ├── Recommendations Page
        └── Dashboard Page
```

---

## Technologies Used

- Python
- Flask
- Pandas
- NumPy
- Scikit-learn
- SciPy
- Plotly
- Matplotlib
- HTML
- CSS
- Jinja2
- Jupyter Notebook

---

## Project Structure

```text
OVIU-Recommendation-System/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│   └── online_retail.csv
│
├── models/
│   ├── popular_products.json
│   ├── item_recommendations.json
│   ├── customer_products.json
│   ├── product_index.json
│   ├── dashboard_data.json
│   ├── product_catalog.json
│   ├── product_lookup.json
│   ├── content_based_recommendations.json
│   ├── collaborative_recommendations.json
│   ├── matrix_factorization_recommendations.json
│   ├── market_basket_recommendations.json
│   ├── customer_segments.json
│   └── ml_model_summary.json
│
├── notebooks/
│   └── OVIU_ML_Recommendation_Analysis.ipynb
│
├── services/
│   └── recommender_service.py
│
├── templates/
│   ├── index.html
│   ├── shop.html
│   ├── product_detail.html
│   ├── cart.html
│   ├── recommendations.html
│   └── dashboard.html
│
└── static/
    └── style.css
```

---

## Installation and Setup

### 1. Create Virtual Environment

```bash
python -m venv venv
```

### 2. Activate Virtual Environment

For Windows PowerShell:

```bash
venv\Scripts\activate
```

For macOS/Linux:

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## How to Run the Project

### 1. Add Dataset

Place the dataset file inside the data folder:

```text
data/online_retail.csv
```

### 2. Run the Jupyter Notebook

Open and run:

```text
notebooks/OVIU_ML_Recommendation_Analysis.ipynb
```

This notebook generates the required model files inside the models folder.

### 3. Run Flask Website

```bash
python app.py
```

Open in browser:

```text
http://127.0.0.1:5000
```

---

## Important Website Routes

| Page | URL |
|---|---|
| Home | `/` |
| Shop | `/shop` |
| Product Detail | `/product/<stock_code>` |
| Cart | `/cart` |
| Recommendations | `/recommendations` |
| Dashboard | `/dashboard` |

---

## Sample Test Inputs

Product search examples:

```text
HEART
BAG
LUNCH BOX
CHRISTMAS
WHITE
RED
MUG
BOX
```

Customer ID example:

```text
13085
```

---

## Generated Model Files

| File | Purpose |
|---|---|
| popular_products.json | Stores best-selling products |
| market_basket_recommendations.json | Stores frequently bought together recommendations |
| content_based_recommendations.json | Stores TF-IDF content-based recommendations |
| collaborative_recommendations.json | Stores collaborative filtering recommendations |
| matrix_factorization_recommendations.json | Stores TruncatedSVD recommendations |
| customer_segments.json | Stores K-Means customer segments |
| product_catalog.json | Stores product catalog for shop page |
| product_lookup.json | Stores product details by stock code |
| dashboard_data.json | Stores dashboard summary data |
| ml_model_summary.json | Stores summary of ML techniques |

---

## Business Value

This project demonstrates how machine learning can support an e-commerce business by:

- Improving product discovery
- Supporting personalized recommendations
- Increasing cross-selling opportunities
- Identifying high-value customer segments
- Understanding customer behavior
- Helping business teams analyze sales trends
- Creating a better shopping experience

---

## Limitations

- The dataset does not include product images.
- The website uses placeholder icons instead of real product images.
- The cart is a simulation and does not process real payments.
- The project does not include user authentication.
- Recommendations are generated from historical transaction data.
- The system does not yet store new live user behavior in a database.

---

## Future Improvements

- Add real product images
- Add user login and customer profiles
- Add checkout and payment simulation
- Store cart and orders in a database
- Add rating-based recommendations
- Add admin panel for product management
- Deploy website online
- Add real-time recommendation updates
- Improve recommendation quality using advanced models

---

## Project Status

Completed prototype with:

- Flask e-commerce website
- Product catalog
- Cart simulation
- Hybrid ML recommendation system
- Customer segmentation
- Analytics dashboard
- Jupyter Notebook ML workflow
- Website integration with generated model files

---

## Author

Abhi Patel

Project: OVIU Hybrid Product Recommendation System