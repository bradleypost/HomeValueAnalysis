import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# Read the CSV file into zhvi_df
zhvi_df = pd.read_csv(r"C:\Users\Bradley\PycharmProjects\HomeValueAnalysis\ZHVI by County.csv")

# Convert the 'Date' column to datetime format
zhvi_df['Date'] = pd.to_datetime(zhvi_df['Date'])
zhvi_df.rename(columns={'Combined': 'Region'}, inplace=True)

# Filter the data for Orange County, FL
orange_county_fl = zhvi_df.loc[zhvi_df['Region'] == 'Orange County, FL']
orange_county_fl = orange_county_fl.dropna(subset=['ZHVI'])

# Sort the DataFrame by date
orange_county_fl = orange_county_fl.sort_values(by='Date')
print(zhvi_df.head())

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(orange_county_fl['Date'], orange_county_fl['ZHVI'], color='blue', linestyle='-')
plt.title('History of the Zillow Home Value Index: Orange County (Orlando), FL')
plt.xlabel('Date')
plt.ylabel('Home Values in Orange County, FL')
plt.xticks(rotation=45)
plt.tight_layout()
#plt.show()

#20 most expensive counties
latest_date_df = zhvi_df[zhvi_df['Date']== zhvi_df['Date'].max()]
most_expensive_counties = latest_date_df.sort_values(by='ZHVI', ascending=False)

top_20_most_expensive_counties = most_expensive_counties.head(20)

print(top_20_most_expensive_counties.columns)
#bar chart
plt.figure(figsize=(10, 6))
plt.bar(top_20_most_expensive_counties['Region'], top_20_most_expensive_counties['ZHVI'], color='red')
plt.title('Most Expensive Counties in 2024')
plt.xlabel('Most Expensive Counties in 1/2024')
plt.ylabel('Home Value (millions $)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

#Orlando metro area housing market
#filter for the Orlando metro area
orlando_housing_market = zhvi_df.loc[zhvi_df['Metro'] == 'Orlando-Kissimmee-Sanford, FL']
orlando_housing_market = orlando_housing_market.dropna(subset=['ZHVI'])
orlando_housing_market= orlando_housing_market.sort_values(by='Date')

#Graph the most expensive counties in the Orlando area over time
counties = orlando_housing_market['Region'].unique()

cmap = cm.get_cmap('tab10')

plt.figure(figsize=(10, 6))

#iterate through the counties
for i, county in enumerate(counties):
    county_data = orlando_housing_market[orlando_housing_market['Region'] == county]
    color = cmap(i % 10)
    plt.plot(county_data['Date'], county_data['ZHVI'], label=county, color=color)

plt.title('History of house prices for the Orlando metro area (2000-2024)')
plt.legend()
plt.xlabel('Date')
plt.ylabel('Home Values, Orlando Metro Area')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
