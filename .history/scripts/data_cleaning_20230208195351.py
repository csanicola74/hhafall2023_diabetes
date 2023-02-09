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

######## ADMISSION TYPE ########
admission_type_map = {'3': 1, '1': 2, '4': 3,
                      '5': 999, '8': 999, '6': 999, '7': 4, '2': 5}

df['admission_type_id'] = df['admission_type_id'].map(admission_type_map)

print(df['admission_type_id'])

######## DISCHARGE DISPOSITION ########
discharge_disposition_map = {'?': 999, 'Discharged to home': 1,
                             'Discharged/transferred to another short term hospital': 2,
                             'Discharged/transferred to SNF': 3,
                             'Discharged/transferred to ICF': 4,
                             'Discharged/transferred to another type of inpatient care institution': 5,
                             'Discharged/transferred to home with home health service': 6,
                             'Left AMA': 7,
                             'Discharged/transferred to home under care of Home IV provider': 8,
                             'Admitted as an inpatient to this hospital': 9,
                             'Neonate discharged to another hospital for neonatal aftercare': 10,
                             'Expired': 11,
                             'Still patient or expected to return for outpatient services': 12,
                             'Hospice / home': 13,
                             'Hospice / medical facility': 14,
                             'Discharged/transferred within this institution to Medicare approved swing bed': 15,
                             'Discharged/transferred/referred another institution for outpatient services': 16,
                             'Discharged/transferred/referred to this institution for outpatient services': 17,
                             'NULL': 999,
                             'Expired at home. Medicaid only, hospice.': 18,
                             'Expired in a medical facility. Medicaid only, hospice.': 19,
                             'Expired, place unknown. Medicaid only, hospice.': 20,
                             'Discharged/transferred to another rehab fac including rehab units of a hospital .': 21,
                             'Discharged/transferred to a long term care hospital.': 22,
                             'Discharged/transferred to a nursing facility certified under Medicaid but not certified under Medicare.': 23,
                             'Not Mapped': 999,
                             'Unknown/Invalid': 999,
                             'Discharged/transferred to a federal health care facility.': 24,
                             'Discharged/transferred/referred to a psychiatric hospital of psychiatric distinct part unit of a hospital': 25,
                             'Discharged/transferred to a Critical Access Hospital (CAH).': 26}

df['discharge_disposition_id'] = df['discharge_disposition_id'].map(
    discharge_disposition_map)

print(df['discharge_disposition_id'])

######## ADMISSION SOURCE ########
admission_source_map = {'?': 999, 'Physician Referral': 1,
                        'Clinic Referral': 2,
                        'HMO Referral': 3,
                        'Transfer from a hospital': 4,
                        'Transfer from a Skilled Nursing Facility (SNF)': 5,
                        'Transfer from another health care facility': 6,
                        'Emergency Room': 7,
                        'Court/Law Enforcement': 8,
                        'Not Available': 999,
                        'Transfer from critial access hospital': 9,
                        'Normal Delivery': 10,
                        'Premature Delivery': 11,
                        'Sick Baby': 12,
                        'Extramural Birth': 13,
                        'Not Available': 999,
                        'NULL': 999,
                        'Transfer From Another Home Health Agency': 14,
                        'Readmission to Same Home Health Agency': 15,
                        'Not Mapped': 999,
                        'Unknown/Invalid': 999,
                        'Transfer from hospital inpt/same fac reslt in a sep claim': 16,
                        'Born inside this hospital': 17,
                        'Born outside this hospital': 18,
                        'Transfer from Ambulatory Surgery Center': 19,
                        'Transfer from Hospice': 20}

df['admission_source_id'] = df['admission_source_id'].map(admission_source_map)

print(df['admission_source_id'])

######## MEDICAL SPECIALTY ########
