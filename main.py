import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/blinkit_orders.csv")
print(df.head())
print(df.shape)
print(df.columns)
print(df.info())
print(df.describe())
print(df["delivery_status"].value_counts())

df["delivery_status"].value_counts().plot(kind="bar")
plt.title("Delivery Status")
plt.xlabel("Status")
plt.ylabel("No of Orders")
plt.show()
print(df["payment_method"].value_counts())

df["payment_method"].value_counts().plot(kind="pie", autopct="%1.1f%%")
plt.title("Payment Method Distribution")
plt.ylabel("")
plt.show()

print(df.groupby("delivery_status")["order_total"].mean())

df.groupby("delivery_status")["order_total"].mean().plot(kind="bar")

plt.title("Average Order Value by Delivery Status")
plt.xlabel("Delivery Status")
plt.ylabel("Average Order Total")
plt.show()

print(df["store_id"].value_counts().head(10))

df["store_id"].value_counts().head(10).plot(kind="bar")

plt.title("Top 10 Stores by Number of Orders")
plt.xlabel("Store ID")
plt.ylabel("Number of Orders")
plt.show()

print(df["delivery_partner_id"].value_counts().head(10))

df["delivery_partner_id"].value_counts().head(10).plot(kind="bar")

plt.title("Top 10 Delivery Partners")
plt.xlabel("Delivery Partner ID")
plt.ylabel("Number of Deliveries")
plt.show()

print(df[["order_date",
          "promised_delivery_time",
          "actual_delivery_time"]].head())

# Convert to datetime
df["promised_delivery_time"] = pd.to_datetime(df["promised_delivery_time"])
df["actual_delivery_time"] = pd.to_datetime(df["actual_delivery_time"])

# Delay in minutes
df["delay_minutes"] = (
    df["actual_delivery_time"] - df["promised_delivery_time"]
).dt.total_seconds() / 60

print(df[["delivery_status", "delay_minutes"]].head())
print(df["delay_minutes"].describe())

df["delay_minutes"].plot(kind="hist", bins=20)

plt.title("Distribution of Delivery Delay")
plt.xlabel("Delay (Minutes)")
plt.ylabel("Number of Orders")
plt.show()

print(
    df.sort_values("delay_minutes", ascending=False)[
        ["order_id", "delivery_status", "delay_minutes"]
    ].head(10)
)

print(df.groupby("delivery_status")["delay_minutes"].mean())

df.groupby("delivery_status")["delay_minutes"].mean().plot(kind="bar")

plt.title("Average Delay by Delivery Status")
plt.xlabel("Delivery Status")
plt.ylabel("Average Delay (Minutes)")
plt.show()

print(
    df.sort_values(by="delay_minutes", ascending=False)
      [["order_id", "delivery_status", "delay_minutes"]]
      .head(10)
)

df.sort_values(by="delay_minutes", ascending=False)\
  .head(10)\
  .plot(
      x="order_id",
      y="delay_minutes",
      kind="bar"
  )

plt.title("Top 10 Most Delayed Orders")
plt.xlabel("Order ID")
plt.ylabel("Delay (Minutes)")
plt.show()

print(df.groupby("payment_method")["order_total"].mean())

df.groupby("payment_method")["order_total"].mean().plot(kind="bar")

plt.title("Average Order Value by Payment Method")
plt.xlabel("Payment Method")
plt.ylabel("Average Order Value")
plt.show()

print(df["store_id"].value_counts().head(10))

df["store_id"].value_counts().head(10).plot(kind="bar")

plt.title("Top 10 Stores by Number of Orders")
plt.xlabel("Store ID")
plt.ylabel("Number of Orders")
plt.show()

print(df.nlargest(10, "order_total")[["order_id", "order_total"]])

print(df.nsmallest(10, "order_total")[["order_id", "order_total"]])

print(pd.crosstab(df["payment_method"], df["delivery_status"]))

pd.crosstab(
    df["payment_method"],
    df["delivery_status"]
).plot(kind="bar")

plt.title("Payment Method vs Delivery Status")
plt.xlabel("Payment Method")
plt.ylabel("Number of Orders")
plt.show()

print("===== PROJECT SUMMARY =====")

print("Total Orders:", len(df))

print("\nDelivery Status:")
print(df["delivery_status"].value_counts())

print("\nPayment Methods:")
print(df["payment_method"].value_counts())

print("\nAverage Order Value:")
print(round(df["order_total"].mean(), 2))

print("\nAverage Delay (Minutes):")
print(round(df["delay_minutes"].mean(), 2))

