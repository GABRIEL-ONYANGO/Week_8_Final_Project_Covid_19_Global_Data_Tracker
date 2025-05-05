# COVID-19 Global Data Tracker
#Data Loading & Exploration
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Loading dataset
df = pd.read_csv('owid-covid-data.csv')

# Basic exploration
print(df.columns)
print(df.head())
print(df.isnull().sum())

# 3. Data Cleaning
# Filtering countries of interest
countries = ['Kenya', 'United States', 'India']
df = df[df['location'].isin(countries)]

# Droping rows with missing date or total_cases
df = df.dropna(subset=['date', 'total_cases'])
df['date'] = pd.to_datetime(df['date'])

# Filling numeric missing values
numeric_cols = ['total_deaths', 'new_cases', 'new_deaths', 'total_vaccinations']
df[numeric_cols] = df[numeric_cols].fillna(0)

# 4. Exploratory Data Analysis (EDA)
plt.figure(figsize=(12,6))
for country in countries:
    country_data = df[df['location'] == country]
    plt.plot(country_data['date'], country_data['total_cases'], label=country)
plt.title('Total COVID-19 Cases Over Time')
plt.xlabel('Date')
plt.ylabel('Total Cases')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Daily new cases comparison
plt.figure(figsize=(12,6))
for country in countries:
    country_data = df[df['location'] == country]
    plt.plot(country_data['date'], country_data['new_cases'], label=country)
plt.title('Daily New Cases Over Time')
plt.xlabel('Date')
plt.ylabel('New Cases')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Death rate over time
for country in countries:
    country_data = df[df['location'] == country].copy()
    country_data['death_rate'] = country_data['total_deaths'] / country_data['total_cases']
    plt.plot(country_data['date'], country_data['death_rate'], label=country)
plt.title('COVID-19 Death Rate Over Time')
plt.xlabel('Date')
plt.ylabel('Death Rate')
plt.legend()
plt.tight_layout()
plt.show()

# 5. Visualizing Vaccination Progress
plt.figure(figsize=(12,6))
for country in countries:
    country_data = df[df['location'] == country]
    plt.plot(country_data['date'], country_data['total_vaccinations'], label=country)
plt.title('Total Vaccinations Over Time')
plt.xlabel('Date')
plt.ylabel('Total Vaccinations')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# 6. Optional: Choropleth Map (Latest Data)
latest_date = df['date'].max()
latest_df = df[df['date'] == latest_date]

choropleth_data = latest_df[['iso_code', 'location', 'total_cases']].dropna()
fig = px.choropleth(choropleth_data, locations='iso_code', color='total_cases',
                    hover_name='location', color_continuous_scale='Reds',
                    title='Total COVID-19 Cases by Country')
fig.show()


