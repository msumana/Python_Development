# Python_Development
# Data Analysis with SQL
# Amazon Sales Data Analysis
# About
This project aims to explore the Amazon Sales data to understand top performing categories and products depending on ratings and reviews. The aim is to study different levels of ratings and their respective reviews which helps to analyze quality of product and strategies to improve products.  

# Purposes Of The Project
The major aim of thie project is to gain insight into the sales data of Amazon to get average ratings of each product category and individual product. Also, analyzing the ratings of highest discount and lowest discount products of each category

# About Data
The dataset was obtained from the Kaggle Amazon Sales Dataset. This dataset contains sales of different regions in USA, products, product categories,time periods of 
transactions,profits. The data contains 10 columns and 3203 rows:

# Column Description Data Type
 #   Column          Dtype         Not Null   Description    
---  ------        --------------  -----         
product_id        VARCHAR(255)     NOT NULL   Product ID
product_name      VARCHAR(2000)    NOT NULL   Name of the Product
category          VARCHAR(2000)    NOT NULL   Category of the Product
discounted_price  DECIMAL(10,2)    NOT NULL   Discounted Price of the Product
actual_price      DECIMAL(10,2)    NOT NULL   Actual Price of the Product
discount_percentage VARCHAR(255)   NOT NULL   Percentage of Discount for the Product 
rating            DECIMAL(10,2)    NOT NULL   Rating of the Product
rating_count      DECIMAL(10,2)    NOT NULL   Number of people who voted for the Amazon rating  
about_product     VARCHAR(4000)    NOT NULL   Description about the Product
user_id           VARCHAR(4000)    NOT NULL   ID of the user who wrote review for the Product
user_name         VARCHAR          NOT NULL   Name of the user who wrote review for the Product
review_id         VARCHAR          NOT NULL   ID of the user review
review_title      VARCHAR          NOT NULL   Short review
review_content    VARCHAR          NOT NULL   Long review
img_link          VARCHAR          NOT NULL   Image Link of the Product
product_link      VARCHAR          NOT NULL   Official Website Link of the Product

# Analysis List
# Product Analysis
Conduct analysis on the data to understand the different product categories, the products categories performing best and the product lines that need to be improved.

# Price Analysis


# Customer Analysis
This analysis aims to answer the question of the products of product category.

# Approach Used
Data Wrangling: This is the first step where inspection of data is done to make sure NULL values and missing values are detected and data replacement methods are used to replace, missing or NULL values.
1. Build a database
2. Create table and insert the data.
3. Select columns with null values in them. There are no null values in our database as in creating the tables, we set NOT NULL for each field, hence null values are filtered out.

# Conclusion:

# Business Questions To Answer
# Generic Question
1. 
