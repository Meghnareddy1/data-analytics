import pandas as pd
import matplotlib.pyplot as plt

# load dataset
data = pd.read_csv("flights.csv")

# remove rows where arrival delay is missing
data = data.dropna(subset=["ARRIVAL_DELAY"])

# group by airline
delay_by_airline = data.groupby("AIRLINE")["ARRIVAL_DELAY"].mean()

print(delay_by_airline)

# create chart
delay_by_airline.sort_values().plot(kind="bar")

plt.title("Average Flight Delay by Airline")
plt.xlabel("Airline")
plt.ylabel("Delay (minutes)")

plt.show()
# average delay by origin airport
delay_by_airport = data.groupby("ORIGIN_AIRPORT")["ARRIVAL_DELAY"].mean()

# get top 10 airports with highest delays
top_airports = delay_by_airport.sort_values(ascending=False).head(10)

print("Top 10 airports with highest delays:")
print(top_airports)

# plot chart
top_airports.plot(kind="bar")

plt.title("Top 10 Airports with Highest Flight Delays")
plt.xlabel("Airport")
plt.ylabel("Average Delay (minutes)")

plt.show()
# delay by month
delay_by_month = data.groupby("MONTH")["ARRIVAL_DELAY"].mean()

print(delay_by_month)

delay_by_month.plot(kind="line", marker="o")

plt.title("Average Flight Delay by Month")
plt.xlabel("Month")
plt.ylabel("Average Delay")

plt.show()
import seaborn as sns

sns.scatterplot(x=data["DISTANCE"], y=data["ARRIVAL_DELAY"])

plt.title("Flight Distance vs Arrival Delay")

plt.show()

'''import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("flights.csv")

data = data.dropna(subset=["ARRIVAL_DELAY"])

delay_by_airline = data.groupby("AIRLINE")["ARRIVAL_DELAY"].mean()

delay_by_airline.sort_values().plot(kind="bar")

plt.title("Average Flight Delay by Airline")
plt.xlabel("Airline")
plt.ylabel("Delay (minutes)")
plt.show()'''

# FINAL STEP
data.to_csv("clean_flight_data.csv", index=False)
print("Cleaned dataset exported successfully!")