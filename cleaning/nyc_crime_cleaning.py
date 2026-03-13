import pandas as pd
import numpy as np

# path to data
path = "INSERT YOUR FILE PATH TO DATASET"

# path to export cleaned data
export_path = "INSERT YOUR FILE PATH TO DATASET"

# 12/35 columns loaded
cols_to_load = ['CMPLNT_FR_DT', 'CMPLNT_FR_TM', 'RPT_DT', 'OFNS_DESC', 'LAW_CAT_CD', 'BORO_NM', 'SUSP_AGE_GROUP', 'SUSP_RACE', 'SUSP_SEX', 'VIC_AGE_GROUP', 'VIC_RACE', 'VIC_SEX']

# null values in dataset
na_values = ['(null)']

# load dataset, using columns, and set '(null)' as NaN
df = pd.read_csv(path, usecols=cols_to_load, low_memory=False, na_values=na_values)

#drop null rows with null values in specified columns
df = df.dropna(subset= ['CMPLNT_FR_DT', 'OFNS_DESC', 'BORO_NM', 'CMPLNT_FR_TM'])

# convert column to datetime type
df['CMPLNT_FR_DT'] = pd.to_datetime(df['CMPLNT_FR_DT'])
df['CMPLNT_FR_TM'] = pd.to_datetime(df['CMPLNT_FR_TM'], format='%H:%M:%S')
df['RPT_DT'] = pd.to_datetime(df['RPT_DT'])

# Check data types of columns
print(df.dtypes)

# Replace invalid values in VIC_SEX with null
df['VIC_SEX'] = df['VIC_SEX'].replace({'D': np.nan, 'E': np.nan, 'L': np.nan})

# Check unique values in VIC_SEX
print(df['VIC_SEX'].unique())

# export clean dataframe to a new CSV
df.to_csv(export_path, index=False)
