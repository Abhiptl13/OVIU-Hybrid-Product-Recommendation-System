# OVIU Hybrid Product Recommendation System for an E-Commerce Purchasing Website

OVIU is a Flask-based e-commerce style product purchasing website integrated with a hybrid machine learning recommendation system. The project uses an online retail transaction dataset to analyze customer purchase behavior, generate product recommendations, simulate shopping cart functionality, and display business insights through an analytics dashboard.

The main purpose of this project is to demonstrate how machine learning techniques can be integrated into a real product purchasing website to improve product discovery, customer personalization, and business decision-making.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Problem Statement](#problem-statement)
- [Project Objectives](#project-objectives)
- [Dataset Information](#dataset-information)
- [Machine Learning Techniques](#machine-learning-techniques)
- [Website Features](#website-features)
- [System Architecture](#system-architecture)
- [Project Workflow](#project-workflow)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Installation and Setup](#installation-and-setup)
- [How to Run the Project](#how-to-run-the-project)
- [Sample Test Inputs](#sample-test-inputs)
- [Generated Model Files](#generated-model-files)
- [Limitations](#limitations)
- [Future Improvements](#future-improvements)
- [Project Status](#project-status)

---

## Project Overview

OVIU is designed as a product purchasing platform where users can browse products, view product details, add products to a cart, and receive personalized product recommendations.

Unlike a simple dashboard project, this system connects machine learning output directly with website functionality. Recommendations are shown inside the product purchasing flow, especially on the product detail page, recommendations page, and cart-related sections.

The website includes:

- Product catalog
- Product search
- Category filtering
- Product detail page
- Add-to-cart simulation
- Cart page
- Product-based recommendations
- Customer-based recommendations
- Customer segmentation
- Analytics dashboard
- Hybrid ML recommendation sections

---

## Problem Statement

Online product purchasing websites often contain many products, making it difficult for users to quickly find relevant items. Without recommendation systems, users may only browse manually or view generic popular products.

This project addresses that problem by building a hybrid recommendation system that suggests products based on:

- Product similarity
- Customer purchase behavior
- Frequently bought together patterns
- Hidden customer-product relationships
- Customer segments
- Product popularity

The goal is to improve product discovery and create a more personalized shopping experience.

---

## Project Objectives

The main objectives of this project are:

1. Build an e-commerce style product purchasing website.
2. Clean and process online retail transaction data.
3. Generate a product catalog from real transaction data.
4. Implement multiple machine learning recommendation techniques.
5. Display recommendations directly inside the website.
6. Create a dashboard for business insights.
7. Simulate cart and purchasing behavior.
8. Present a complete portfolio-ready AI/ML web application.

---

## Dataset Information

The project uses an online retail transaction dataset.

### Main Dataset Columns

| Column | Description |
|---|---|
| Invoice | Unique invoice or transaction number |
| StockCode | Product stock code |
| Description | Product name or product description |
| Quantity | Number of items purchased |
| InvoiceDate | Date and time of invoice |
| Price | Unit price of the product |
| Customer ID | Customer identifier |
| Country | Customer country |

### Dataset Usage

The dataset is used for:

- Product catalog generation
- Product popularity analysis
- Customer purchase history
- Market basket analysis
- Collaborative filtering
- Matrix factorization
- Customer segmentation
- Dashboard analytics

### Important Dataset Note

The dataset does not include product image URLs. Because of this, the website uses category-based placeholder visuals and icons for product cards.

The recommendation system itself does not require product images because the machine learning models use transaction data, product descriptions, customer IDs, quantity, invoice history, and price.

---

## Machine Learning Techniques

This project uses multiple recommendation and machine learning techniques to create a hybrid recommendation system.

---

### 1. Popularity-Based Recommendation

Popularity-based recommendation is used as a baseline recommendation method.

It recommends products based on:

- Total quantity sold
- Total number of orders
- Total revenue

This method is useful for showing trending or best-selling products.

Example:

> Recommend the top-selling products to new users who do not have purchase history.

---

### 2. Market Basket Analysis

Market basket analysis identifies products that are frequently purchased together in the same invoice or shopping basket.

This method answers questions like:

> Customers who bought Product A also bought Product B.

The system groups products by invoice number and counts product co-occurrence patterns.

This is useful for:

- Add-on recommendations
- Cart recommendations
- Cross-selling
- Frequently bought together products

---

### 3. Content-Based Filtering

Content-based filtering recommends products based on product description similarity.

Techniques used:

- TF-IDF Vectorization
- Cosine Similarity

Product descriptions are converted into numerical vectors using TF-IDF. Then cosine similarity is used to find products with similar text features.

Example:

If a user views a product containing words like `heart`, `white`, or `holder`, the system recommends products with similar description patterns.

---

### 4. Item-Based Collaborative Filtering

Item-based collaborative filtering uses customer-product purchase behavior.

Technique used:

- Customer-product interaction matrix
- Cosine similarity

The system creates a matrix where rows represent customers and columns represent products. The values represent customer interaction with products, such as purchase quantity.

Then product similarity is calculated based on customer purchase behavior.

This helps recommend products that are purchased by similar customers.

---

### 5. Matrix Factorization

Matrix factorization is used to learn hidden relationships between customers and products.

Technique used:

- TruncatedSVD

The customer-product matrix is reduced into latent features. These hidden features represent patterns that may not be visible from direct product descriptions or simple co-purchase counts.

This method helps discover deeper similarity between products.

---

### 6. Customer Segmentation

Customer segmentation groups customers based on purchase behavior.

Technique used:

- K-Means Clustering

Customer features include:

- Total spending
- Total orders
- Total quantity purchased
- Number of unique products purchased
- Average product price
- Average order value

The system groups customers into segments such as:

- High Value Customers
- Frequent Buyers
- Regular Customers
- Low Activity Customers

This is useful for personalized marketing and customer behavior analysis.

---

## Website Features

---

### Home Page

 that may not be visible from direct product descriptions or simple co-purchase counts.

This method helps discover deeper similarity between products.

---

### 6. Customer Segmentation

Customer segmentation groups customers based on purchase behavior.

Technique used:

- K-Means Clustering

Customer features include:

- Total spending
- Total orders
- Total quantity purchased
- Number of unique products purchased
- Average product price
- Average order value

The system groups customers into segments such as:

-The home page introduces the OVIU recommendation system and shows top products from the dataset.

Features:

- Project introduction
- Call-to-action buttons
- Top product preview
- Explanation of recommendation system purpose

---

### Shop Page

The shop page displays products generated from the cleaned retail dataset.

Features:

- Product catalog
- Product search
- Category filter
- Product cards
- Product price
- Stock code
- Placeholder product visual
- View product button
- Add to cart button

---

### Product Detail Page

The product detail page shows product information and ML-powered recommendations.

Features:

- Product name
- Product stock code
- Product price
- Total sold
- Number of orders
- Revenue
- Add to cart button
- ML recommendation sections

Recommendation sections include:

- Content-Based Filtering
- Collaborative Filtering
- Matrix Factorization
- Market Basket Analysis

This page is important because it proves that the ML system is integrated into the purchasing website.

---

### Cart Page

The cart page simulates a product purchasing flow.

Features:

- Added products
- Quantity
- Product price
- Item total
- Cart total
- Remove product button
- Clear cart button
- Recommended add-ons

---

### Recommendations Page

The recommendations page allows users to test recommendation models manually.

Features:

- Product-based recommendation input
- Customer-based recommendation input
- Recommended products
- ML method name
- Recommendation score
- Customer purchase history
- Customer segment from K-Means clustering

Sample inputs:

- Product: HEART
- Product: BAG
- Product: LUNCH BOX
- Customer ID: 13085

---

### Dashboard Page

The dashboard page provides analytics from the cleaned dataset.

Features:

- Total transactions
- Total products
- Total customers
- Total revenue
- Top-selling products
- Top countries by revenue
- Monthly revenue trend
- Plotly charts
- Data tables

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

## Project Workflow

### Step 1: Data Loading

The dataset is loaded using Pandas.

### Step 2: Data Cleaning

The cleaning process includes:

- Renaming columns
- Removing cancelled invoices
- Removing missing product descriptions
- Removing invalid quantities
- Removing invalid prices
- Converting invoice dates
- Creating total price column

### Step 3: Product Catalog Generation

A product catalog is generated from the transaction dataset using:

- Stock code
- Product description
- Median price
- Total quantity sold
- Total revenue
- Number of orders
- Category detection
- Placeholder icon generation

### Step 4: Model Training

The notebook trains multiple recommendation models and saves model outputs as JSON files.

### Step 5: Website Integration

The Flask service layer loads the JSON model files and provides recommendations to the website pages.

### Step 6: User Interaction

Users can browse products, add items to cart, view recommendations, and analyze business insights through the dashboard.

---

## Technologies Used

### Programming and Backend

- Python
- Flask

### Data Processing

- Pandas
- NumPy

### Machine Learning

- Scikit-learn
- SciPy
- TF-IDF Vectorizer
- Cosine Similarity
- TruncatedSVD
- K-Means Clustering
- StandardScaler

### Visualization

- Plotly
- Matplotlib

### Frontend

- HTML
- CSS
- Jinja2 templates

### Development Tools

- Jupyter Notebook
- VS Code
- GitHub

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

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd OVIU-Recommendation-System
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

For Windows PowerShell:

```bash
venv\Scripts\activate
```

For macOS/Linux:

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## How to Run the Project

### 1. Add Dataset

Place the dataset file in the `data/` folder:

```text
data/online_retail.csv
```

### 2. Run the Jupyter Notebook

Open and run:

```text
notebooks/OVIU_ML_Recommendation_Analysis.ipynb
```

This notebook generates the required JSON model files inside the `models/` folder.

### 3. Run Flask Website

```bash
python app.py
```

Open the website in browser:

```text
http://127.0.0.1:5000
```

---

## Important Pages

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

### Product-Based Recommendation

Try these product keywords:

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

### Customer-Based Recommendation

Try this customer ID:

```text
13085
```

---

## Generated Model Files

The notebook creates these files inside the `models/` folder:

| File | Purpose |
|---|---|
| popular_products.json | Stores best-selling products |
| market_basket_recommendations.json | Stores frequently bought together recommendations |
| content_based_recommendations.json | Stores TF-IDF content-based recommendations |
| collaborative_recommendations.json | Stores item-based collaborative filtering recommendations |
| matrix_factorization_recommendations.json | Stores TruncatedSVD recommendations |
| customer_segments.json | Stores K-Means customer segments |
| product_catalog.json | Stores product catalog for shop page |
| product_lookup.json | Stores product details by stock code |
| dashboard_data.json | Stores dashboard summary data |
| ml_model_summary.json | Stores summary of ML techniques |

---

## Recommendation Output Example

For a selected product, the product detail page can display:

```text
Content-Based Filtering:
- Similar products based on product description text

Collaborative Filtering:
- Products purchased by similar customers

Matrix Factorization:
- Products discovered through hidden purchase patterns

Market Basket Analysis:
- Products frequently bought together
```

---

## Business Value

This project demonstrates how machine learning can support an e-commerce business by:

- Improving product discovery
- Increasing cross-selling opportunities
- Supporting personalized recommendations
- Understanding customer behavior
- Identifying high-value customer segments
- Helping business teams analyze sales trends
- Creating a better shopping experience

---

## Limitations

- The dataset does not include product images.
- The website uses placeholder icons instead of real product images.
- The cart is a simulation and does not process real payments.
- The project does not include user authentication.
- Recommendations are generated from historical transaction patterns only.
- The system does not store new user behavior in a live database yet.

---

## Future Improvements

Possible future improvements include:

- Add real product images
- Add user login and customer profiles
- Store cart and orders in a database
- Add checkout and payment simulation
- Add rating-based recommendations
- Add real-time recommendation updates
- Add admin panel for product management
- Deploy the website online
- Use database storage instead of static JSON files
- Add product reviews and feedback
- Improve recommendation quality using advanced deep learning models

---

## Deployment Notes

For deployment, the Flask app can be hosted on platforms such as Render.

Recommended start command:

```bash
gunicorn app:app
```

Recommended build command:

```bash
pip install -r requirements.txt
```

Large dataset files should not be pushed to GitHub if they exceed GitHub file size limits. The generated model JSON files can be included if they are small enough for deployment.

---

## Project Status

Completed prototype with:

- E-commerce style Flask website
- Product catalog
- Cart simulation
- Hybrid ML recommendation system
- Customer segmentation
- Analytics dashboard
- Jupyter Notebook for ML workflow
- Website integration with generated model files

---

## Author

Abhi Patel

Project: OVIU Hybrid Product Recommendation System
