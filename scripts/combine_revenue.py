import pandas as pd
import os

path = os.path.expanduser('~/Desktop/ecommerce-customer-analytics/data/processed/')

# Load historical monthly revenue
hist = pd.read_csv(path + 'monthly_revenue.csv', parse_dates=['date'])
hist = hist[['date', 'revenue']].copy()
hist['type'] = 'Historical'

# Load forward forecast
fcast = pd.read_csv(path + 'revenue_forecast.csv', parse_dates=['date'])
fcast = fcast[['date', 'revenue']].copy()
fcast['type'] = 'Forecast'

# Combine and sort chronologically
combined = pd.concat([hist, fcast]).sort_values('date').reset_index(drop=True)

# Save to processed folder
output = path + 'revenue_combined.csv'
combined.to_csv(output, index=False)

print(f'Done! File saved to: {output}')
print(f'Rows: {len(combined)} ({len(hist)} historical + {len(fcast)} forecast)')
print(combined.tail(6).to_string(index=False))
