import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# load dataset
data = pd.read_csv("sales_analysis_project/tips.csv")

print(data.head())

# total sales by day
sales_by_day = data.groupby("day")["total_bill"].sum()

sales_by_day.plot(kind="bar")

plt.title("Total Sales by Day")
plt.xlabel("Day")
plt.ylabel("Revenue")

plt.show()

# average tip by day
avg_tip = data.groupby("day")["tip"].mean()

avg_tip.plot(kind="bar")

plt.title("Average Tip by Day")
plt.xlabel("Day")
plt.ylabel("Average Tip")

plt.show()

# customer size vs spending
sns.barplot(x="size", y="total_bill", data=data)

plt.title("Customer Group Size vs Spending")

plt.show()
data.to_csv("sales_clean_data.csv", index=False)