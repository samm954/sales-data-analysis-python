import pandas as pd
import matplotlib.pyplot as plt
data={
    "City":["Delhi", "Mumbai", "Delhi", "Mumbai", "Delhi"],
    "Product":["Laptop", "Mobile", "Mobile", "Laptop", "Tablet"],
    "Sales":[50000, 30000, 20000, 45000, 15000]
}
df=pd.DataFrame(data)
print(df)

#city wise sales
city_sales=df.groupby("City")["Sales"].sum()
print(city_sales)

#product wise sales
product_sales=df.groupby("Product")["Sales"].sum()
print(product_sales)

#graph visualization
city_sales.plot(kind="bar")

plt.title("City Wise Sales")
plt.xlabel("City")
plt.ylabel("Sales")

plt.show()