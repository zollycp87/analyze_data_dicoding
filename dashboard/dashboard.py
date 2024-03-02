import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Load dataset
day_bike_df = pd.read_csv("../data/day.csv")

# Header
st.title('Bike Rental Dashboard')

# Total orders
total_orders = day_bike_df['cnt'].sum()
# Average daily rentals
average_daily_rentals = day_bike_df['cnt'].mean()
# Display total orders and average daily rentals using columns layout
col1, col2 = st.columns(2)
with col1:
    st.metric("Total Rent", value="{:,.0f}".format(total_orders))
with col2:
    st.metric("Average Rent per day", value="{:.2f}".format(average_daily_rentals))


# Display dataset
st.subheader('Dataset Overview')
day_bike_df['season'] = day_bike_df['season'].replace({1: 'spring', 2: 'summer', 3: 'fall', 4: 'winter'})
day_bike_df['workingday'] = day_bike_df['workingday'].replace({1: 'weekday', 0: 'holiday/weekend'})
st.write(day_bike_df)

# Visualize data
st.subheader('Data Visualization')

# Set layout options
st.set_option('deprecation.showPyplotGlobalUse', False)
st.set_option('deprecation.showfileUploaderEncoding', False)

# Bar plot of total rental bikes per season
st.subheader('Total Rental Bikes per Season')
season_counts = day_bike_df.groupby('season')['cnt'].sum()
st.bar_chart(season_counts)

# Line plot of total rental bikes over time
st.subheader('Total Rental Bikes Over Time')
day_bike_df['dteday'] = pd.to_datetime(day_bike_df['dteday'])
rentals_over_time = day_bike_df.groupby('dteday')['cnt'].sum()
st.line_chart(rentals_over_time)

# Pie chart of holiday vs non-holiday rentals
st.subheader('Holiday vs Non-holiday Rentals')
holiday_counts = day_bike_df['workingday'].value_counts()
fig_holiday, ax_holiday = plt.subplots(figsize=(6, 6))
ax_holiday.pie(holiday_counts, labels=holiday_counts.index, autopct='%1.1f%%', startangle=140)
ax_holiday.set_title('Holiday vs Non-holiday Rentals')
st.pyplot(fig_holiday)

