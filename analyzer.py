import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")

print("DATA:")
print(df)

print("\nSTATISTICS:")

print("Average Sales:", df["Sales"].mean())
print("Highest Sales:", df["Sales"].max())
print("Lowest Sales:", df["Sales"].min())
print("Average Expenses:", df["Expenses"].mean())

print("Average Sales:", df["Sales"].mean())

plt.figure(figsize=(8, 5))

plt.plot(df["Month"], df["Sales"])

plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.savefig("charts line_chart.png")

plt.show()

plt.figure(figsize=(8, 5))

plt.bar(df["Month"], df["Sales"])

plt.title("Monthly Sales - Bar Chart")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.savefig("charts bar_chart.png")

plt.show()



plt.figure(figsize=(7, 7))

plt.pie(
    df["Sales"],
    labels=df["Month"],
    autopct="%1.1f%%"
)

plt.title("Sales Distribution by Month")

plt.savefig("charts pie_chart.png")

plt.show()