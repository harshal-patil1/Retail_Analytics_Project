import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# loading dataset
data = pd.read_csv("data/superstore.csv", encoding="latin1")

# sales by region analysis
region_sales = data.groupby("Region")["Sales"].sum().sort_values(ascending=False)

# creating chart size
plt.figure(figsize=(8,5))

# creating bar chart
sns.barplot(
    x=region_sales.index,
    y=region_sales.values
)

# chart title
plt.title("Sales by Region")

# x-axis label
plt.xlabel("Region")

# y-axis label
plt.ylabel("Total Sales")

# showing chart
plt.show()


# profit by category
category_profit = data.groupby("Category")["Profit"].sum().sort_values(ascending=False)

# creating new figure
plt.figure(figsize=(8,5))

# creating bar chart
sns.barplot(
    x=category_profit.index,
    y=category_profit.values
)

# chart title
plt.title("Profit by Category")

# axis labels
plt.xlabel("Category")
plt.ylabel("Total Profit")

# showing chart
plt.show()


# converting order date into datetime
data["Order Date"] = pd.to_datetime(data["Order Date"])

# extracting month from order date
data["Month"] = data["Order Date"].dt.month_name()

# monthly sales analysis
monthly_sales = data.groupby("Month")["Sales"].sum()

# creating figure
plt.figure(figsize=(10,5))

# line chart
sns.lineplot(
    x=monthly_sales.index,
    y=monthly_sales.values,
    marker="o"
)

# chart title
plt.title("Monthly Sales Trend")

# axis labels
plt.xlabel("Month")
plt.ylabel("Total Sales")

# rotating month labels
plt.xticks(rotation=45)

# showing chart
plt.show()


# top 10 products by sales
top_products = data.groupby("Product Name")["Sales"].sum()

# sorting highest to lowest
top_products = top_products.sort_values(ascending=False).head(10)

# creating figure
plt.figure(figsize=(14,8))

# horizontal bar chart
sns.barplot(
    x=top_products.values,
    y=top_products.index
)

# chart title
plt.title("Top 10 Products by Sales")

# axis labels
plt.xlabel("Total Sales")
plt.ylabel("Product Name")

# adjusting layout
plt.tight_layout()

plt.grid(axis='x')
# showing chart
plt.show()

# sales by customer segment
segment_sales = data.groupby("Segment")["Sales"].sum()

# creating figure
plt.figure(figsize=(7,7))

# pie chart
plt.pie(
    segment_sales.values,
    labels=segment_sales.index,
    autopct='%1.1f%%'
)

# chart title
plt.title("Sales Distribution by Customer Segment")

# showing chart
plt.show()


# selecting numeric columns
numeric_data = data[["Sales", "Profit", "Discount", "Quantity"]]

# correlation matrix
correlation = numeric_data.corr()

# creating figure
plt.figure(figsize=(8,6))

# heatmap
sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm"
)

# chart title
plt.title("Correlation Heatmap")

# showing chart
plt.show()


# creating figure
plt.figure(figsize=(8,5))

# box plot for sales
sns.boxplot(
    x=data["Sales"]
)

# chart title
plt.title("Sales Outlier Analysis")

# showing chart
plt.show()

# creating figure
plt.figure(figsize=(8,5))

# scatter plot
sns.scatterplot(
    x=data["Sales"],
    y=data["Profit"]
)

# chart title
plt.title("Sales vs Profit Relationship")

# axis labels
plt.xlabel("Sales")
plt.ylabel("Profit")

# showing chart
plt.show()


# creating figure
plt.figure(figsize=(8,5))

# scatter plot for discount vs profit
sns.scatterplot(
    x=data["Discount"],
    y=data["Profit"]
)

# chart title
plt.title("Discount vs Profit Analysis")

# axis labels
plt.xlabel("Discount")
plt.ylabel("Profit")

# showing chart
plt.show()

# top 10 customers by sales
top_customers = data.groupby("Customer Name")["Sales"].sum()

# sorting highest to lowest
top_customers = top_customers.sort_values(ascending=False).head(10)

# creating figure
plt.figure(figsize=(12,6))

# horizontal bar chart
sns.barplot(
    x=top_customers.values,
    y=top_customers.index
)

# chart title
plt.title("Top 10 Customers by Sales")

# axis labels
plt.xlabel("Total Sales")
plt.ylabel("Customer Name")

# grid lines
plt.grid(axis='x')

# adjusting layout
plt.tight_layout()

# showing chart
plt.show()

# sub-category profit analysis
subcategory_profit = data.groupby("Sub-Category")["Profit"].sum()

# sorting values
subcategory_profit = subcategory_profit.sort_values()

# creating figure
plt.figure(figsize=(12,7))

# horizontal bar chart
sns.barplot(
    x=subcategory_profit.values,
    y=subcategory_profit.index
)

# chart title
plt.title("Profit by Sub-Category")

# axis labels
plt.xlabel("Total Profit")
plt.ylabel("Sub-Category")

# grid lines
plt.grid(axis='x')

# adjusting layout
plt.tight_layout()

# showing chart
plt.show()