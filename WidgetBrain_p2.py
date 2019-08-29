import pandas as pd

#Import data
data = 'sales data 2019 1-3.xlsx'

#Create dataframe
xlsx = pd.ExcelFile(data)
sales_sheets = []
for sheet in xlsx.sheet_names:
    sales_sheets.append(xlsx.parse(sheet))
    sales=pd.concat(sales_sheets)
    
#Set index as date
sales=sales.set_index('date')

#define resampling parameters
what_to_do={'amount': "sum", 'transaction': "count"}

#resample time series to 15 minutes
sales2=sales.resample(rule='15min',how=what_to_do)

#Export and print
export_csv = sales2.to_csv(r'C:\Users\Vihan Patel\sales_export.csv')
print(sales2.head())