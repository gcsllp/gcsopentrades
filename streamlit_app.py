# Import required libraries
import pandas as pd
import streamlit as st
import plotly.express as px

# Create a sample dataframe
data = {'Date': ['10-10-2023', '10-10-2023', '10-10-2023', '10-10-2023', '10-10-2023', '10-10-2023', '10-10-2023'],
        'Broker': ['HSO', 'DAS', 'HAP', 'MCA', 'MHI', 'TSM', 'KDH'],
        'PnL': [2380.6, 7906.5, 19465.6, 9011.2, 18008, 29309.2, 3331.6],
        'Total': [89413, 89413, 89413, 89413, 89413, 89413, 89413]}

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])  # Convert the Date column to datetime

# Streamlit app
st.title('Broker PnL Dashboard')

# Display data table
st.write("### Data Table")
st.write(df)

# Display a bar chart
st.write("### PnL by Broker on 10-10-2023")
fig = px.bar(df, x='Broker', y='PnL', text='PnL', title='PnL by Broker')
st.plotly_chart(fig)

# Monthly and yearly summary
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month

monthly_summary = df.groupby(['Year', 'Month', 'Broker'])['PnL'].sum().reset_index()
yearly_summary = df.groupby(['Year', 'Broker'])['PnL'].sum().reset_index()

# Display Monthly Summary
st.write("### Monthly PnL Summary")
st.write(monthly_summary.pivot(index='Broker', columns=['Year', 'Month'], values='PnL').fillna(0))

# Monthly PnL bar chart
st.write("### Monthly PnL Bar Chart")
month_selected = st.selectbox('Select Month', monthly_summary['Month'].unique())
monthly_data = monthly_summary[monthly_summary['Month'] == month_selected]
fig_monthly = px.bar(monthly_data, x='Broker', y='PnL', text='PnL', title=f'Monthly PnL for {month_selected}')
st.plotly_chart(fig_monthly)

# Yearly PnL bar chart
st.write("### Yearly PnL Bar Chart")
fig_yearly = px.bar(yearly_summary, x='Broker', y='PnL', text='PnL', title='Yearly PnL by Broker')
st.plotly_chart(fig_yearly)
