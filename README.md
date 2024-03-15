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
 #   Column        Non-Null Count  Dtype         
---  ------        --------------  -----         
 0   Order ID      3203 non-null   object        
 1   Order Date    3203 non-null   datetime64[ns]
 2   Ship Date     3203 non-null   datetime64[ns]
 3   EmailID       3203 non-null   object        
 4   Geography     3203 non-null   object        
 5   Category      3203 non-null   object        
 6   Product Name  3203 non-null   object        
 7   Sales         3203 non-null   float64       
 8   Quantity      3203 non-null   int64         
 9   Profit        3203 non-null   float64    

# Analysis List
# Product Analysis
Conduct analysis on the data to understand the different product categories, the products categories performing best and the product lines that need to be improved.

# Customer Analysis
This analysis aims to answer the question of the sales categories of product. The result of this can help use measure the effectiveness of each sales strategy the business applies and what modificatoins are needed to gain more sales.

# Approach Used
Data Wrangling: This is the first step where inspection of data is done to make sure NULL values and missing values are detected and data replacement methods are used to replace, missing or NULL values.
Build a database
Create table and insert the data.
Select columns with null values in them. There are no null values in our database as in creating the tables, we set NOT NULL for each field, hence null values are filtered out.
Feature Engineering: This will help use generate some new columns from existing ones.
Add varchar for entering unlimited text in ratings,reviews and about product columns

# Conclusion:

# Business Questions To Answer
# Generic Question
1. 
