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

# Index
# (['race',
#   'gender',
#   'age',
#   'admission_type_id',
#   'discharge_disposition_id',
#   'admission_source_id',
#   'time_in_hospital',
#   'medical_specialty',
#   'num_lab_procedures',
#   'num_procedures',
#   'num_medications',
#   'number_outpatient',
#   'number_emergency',
#   'number_inpatient',
#   'diag_1',
#   'diag_2',
#   'diag_3',
#   'number_diagnoses',
#   'max_glu_serum',
#   'A1Cresult',
#   'metformin',
#   'repaglinide',
#   'nateglinide',
#   'chlorpropamide',
#   'glimepiride',
#   'acetohexamide',
#   'glipizide',
#   'glyburide',
#   'tolbutamide',
#   'pioglitazone',
#   'rosiglitazone',
#   'acarbose',
#   'miglitol',
#   'troglitazone',
#   'tolazamide',
#   'insulin',
#   'glyburide-metformin',
#   'glipizide-metformin',
#   'glimepiride-pioglitazone',
#   'metformin-rosiglitazone',
#   'metformin-pioglitazone',
#   'change',
#   'diabetesMed',
#   'readmitted'],
#   dtype='object')


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
