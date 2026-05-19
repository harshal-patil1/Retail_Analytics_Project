
import pandas as pd

# loading dataset with encoding fix
data = pd.read_csv("data/superstore.csv", encoding="latin1")

# sales by region
region_sales = data.groupby("Region")["Sales"].sum()

print(region_sales)

# profit by category
category_profit = data.groupby("Category")["Profit"].sum()

# sorting highest to lowest
category_profit = category_profit.sort_values(ascending=False)

print(category_profit)


# sales by customer segment
segment_sales = data.groupby("Segment")["Sales"].sum()

# sorting highest to lowest
segment_sales = segment_sales.sort_values(ascending=False)

print(segment_sales)





# showing first 5 rows
print(data.head())

# showing total rows and columns
print(data.shape)

# showing all column names
print(data.columns)

# showing dataset information
print(data.info())

# checking null values
print(data.isnull().sum())

# checking duplicate rows
print(data.duplicated().sum())

# removing duplicate rows
data = data.drop_duplicates()

# showing final shape after cleaning
print(data.shape)

# calculating total sales KPI
total_sales = data["Sales"].sum()

print("Total Sales:", total_sales)