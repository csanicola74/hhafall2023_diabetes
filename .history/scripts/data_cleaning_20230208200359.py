###########################
####  IMPORT PACKAGES  ####
###########################

import pandas as pd
import datetime as dt
import uuid
import numpy as np
from datetime import datetime
from datetime import date
import re
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
pd.set_option("max_info_columns", 100)
pd.set_option("max_info_rows", 100)

########################
#### IMPORT DATASET ####
########################

# load in original dataset
df = pd.read_csv('data/diabetic_data_ORIGINAL.csv')

# get a count of the number of rows and columns
print(df.shape)
# (101766, 50)
# preview the first 5 rows of the dataset
df.head()

#################
#### COLUMNS ####
#################

# get column names
df.columns

# drop columns that are not needed
df = df.drop(['encounter_id', 'patient_nbr', 'weight',
             'payer_code', 'examide', 'citoglipton'], axis=1)

# duplicate age column
df['age_grouping'] = df['age']

# duplicate readmitted column
df['readmitted_30'] = df['readmitted']


################
#### VALUES ####
################

# replace string values with numbers
# define the mapping dictionary for each column

######## RACE ########
race_map = {'?': 999, 'AfricanAmerican': 1, 'Asian': 2,
            'Caucasian': 3, 'Hispanic': 4, 'Other': 999}

df['race'] = df['race'].map(race_map)

print(df['race'])

######## GENDER ########
gender_map = {'Female': 1, 'Male': 2, 'Unknown/Invalid': 999}

df['gender'] = df['gender'].map(gender_map)

print(df['gender'])

######## AGE ########
age_map = {'[0-10)': 1, '[10-20)': 2, '[20-30)': 3, '[30-40)': 4,
           '[40-50)': 5, '[50-60)': 6, '[60-70)': 7, '[70-80)': 8,
           '[80-90)': 9, '[90-100)': 10}
age_map_2 = {'[0-10)': 1, '[10-20)': 1, '[20-30)': 1, '[30-40)': 2, '[40-50)': 2,
             '[50-60)': 2, '[60-70)': 2, '[70-80)': 3, '[80-90)': 3, '[90-100)': 3}
df['age'] = df['age'].map(age_map)
df['age_grouping'] = df['age_grouping'].map(age_map_2)

print(df['age'])
print(df['age_grouping'])

######## ADMISSION TYPE ########
admission_type_map = {3: 1, 1: 2, 4: 3, 5: 999, 8: 999, 6: 999, 7: 4, 2: 5}

df['admission_type_id'] = df['admission_type_id'].map(admission_type_map)

print(df['admission_type_id'])

######## DISCHARGE DISPOSITION ########
discharge_disposition_map = {9: 1, 1: 2, 29: 3, 27: 4, 23: 5, 24: 6, 22: 7, 2: 8, 30: 9, 5: 10,
                             8: 11, 6: 12, 4: 13, 3: 14, 15: 15, 16: 16, 28: 17, 17: 18, 11: 19,
                             19: 20, 20: 21, 21: 22, 13: 23, 14: 24, 7: 25, 10: 26, 25: 999, 18: 999, 12: 27, 26: 999}


df['discharge_disposition_id'] = df['discharge_disposition_id'].map(
    discharge_disposition_map)

print(df['discharge_disposition_id'])

######## ADMISSION SOURCE ########
admission_source_map = {23}

df['admission_source_id'] = df['admission_source_id'].map(admission_source_map)

print(df['admission_source_id'])

######## MEDICAL SPECIALTY ########
