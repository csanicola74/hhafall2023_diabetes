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
#   'metformin', 'repaglinide', 'nateglinide', 'chlorpropamide', 'glimepiride', 'acetohexamide', 'glipizide', 'glyburide', 'tolbutamide', 'pioglitazone', 'rosiglitazone', 'acarbose', 'miglitol', 'troglitazone', 'tolazamide', 'insulin', 'glyburide-metformin', 'glipizide-metformin', 'glimepiride-pioglitazone', 'metformin-rosiglitazone', 'metformin-pioglitazone', 'change', 'diabetesMed', 'readmitted'], dtype='object')

# drop columns that are not needed
df = df.drop(['encounter_id', 'patient_nbr', 'weight',
             'payer_code', 'examide', 'citoglipton'], axis=1)

# duplicate age column
df['age'] = df['age_grouping']

# duplicate readmitted column
df['readmitted'] = df['readmitted_30']

################
#### VALUES ####
################

# replace string values with numbers
# define the mapping dictionary for each column

race_map = {'?': 999, 'AfricanAmerican': 1, 'Asian': 2,
            'Caucasian': 3, 'Hispanic': 4, 'Other': 999}

df['race'] = df['race'].map(race_map)


print(df)
