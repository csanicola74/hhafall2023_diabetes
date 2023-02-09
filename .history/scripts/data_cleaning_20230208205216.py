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
admission_source_map = {23: 1, 24: 2, 2: 3, 8: 4, 7: 5, 14: 6, 3: 7, 11: 8, 9: 999, 15: 999, 20: 999,
                        17: 999, 1: 9, 12: 10, 19: 11, 13: 12, 4: 13, 5: 14, 25: 15, 6: 16, 18: 17, 10: 18, 26: 19, 22: 20, 21: 999}

df['admission_source_id'] = df['admission_source_id'].map(admission_source_map)

print(df['admission_source_id'])

######## MEDICAL SPECIALTY ########
medical_specialty_map = {'AllergyandImmunology': 1,
                         'Anesthesiology': 2,
                         'Anesthesiology-Pediatric': 2,
                         'Cardiology': 3,
                         'Cardiology-Pediatric': 3,
                         'DCPTEAM': 18,
                         'Dentistry': 4,
                         'Dermatology': 5,
                         'Emergency/Trauma': 6,
                         'Endocrinology': 7,
                         'Endocrinology-Metabolism': 7,
                         'Family/GeneralPractice': 11,
                         'Gastroenterology': 8,
                         'Gynecology': 14,
                         'Hematology': 9,
                         'Hematology/Oncology': 9,
                         'Hospitalist': 18,
                         'InfectiousDiseases': 10,
                         'InternalMedicine': 11,
                         'Nephrology': 12,
                         'Neurology': 13,
                         'Neurophysiology': 13,
                         'Obsterics&Gynecology-GynecologicOnco': 14,
                         'Obstetrics': 14,
                         'ObstetricsandGynecology': 14,
                         'Oncology': 9,
                         'Ophthalmology': 15,
                         'Orthopedics': 16,
                         'Orthopedics-Reconstructive': 16,
                         'Osteopath': 17,
                         'Otolaryngology': 19,
                         'OutreachServices': 18,
                         'Pathology': 20,
                         'Pediatrics': 11,
                         'Pediatrics-AllergyandImmunology': 1,
                         'Pediatrics-CriticalCare': 6,
                         'Pediatrics-EmergencyMedicine': 6,
                         'Pediatrics-Endocrinology': 7,
                         'Pediatrics-Hematology-Oncology': 9,
                         'Pediatrics-InfectiousDiseases': 10,
                         'Pediatrics-Neurology': 13,
                         'Pediatrics-Pulmonology': 25,
                         'Perinatology': 14,
                         'PhysicalMedicineandRehabilitation': 21,
                         'PhysicianNotFound': 999,
                         'Podiatry': 22,
                         'Proctology': 23,
                         'Psychiatry': 24,
                         'Psychiatry-Addictive': 24,
                         'Psychiatry-Child/Adolescent': 24,
                         'Psychology': 24,
                         'Pulmonology': 25,
                         'Radiologist': 26,
                         'Radiology': 26,
                         'Resident': 18,
                         'Rheumatology': 27,
                         'Speech': 18,
                         'SportsMedicine': 18,
                         'Surgeon': 28,
                         'Surgery-Cardiovascular':  28,
                         'Surgery-Cardiovascular/Thoracic': 28,
                         'Surgery-Colon&Rectal': 28,
                         'Surgery-General': 28,
                         'Surgery-Maxillofacial': 28,
                         'Surgery-Neuro': 28,
                         'Surgery-Pediatric': 28,
                         'Surgery-Plastic': 28,
                         'Surgery-PlasticwithinHeadandNeck': 28,
                         'Surgery-Thoracic': 28,
                         'Surgery-Vascular': 28,
                         'SurgicalSpecialty': 28,
                         'Urology': 29}

df['medical_specialty'] = df['medical_specialty'].map(medical_specialty_map)

print(df['medical_specialty'])

######## LAB PROCEDURES ########


def lab_proc_map(x):
    if x <= 9:
        return 1
    elif x <= 19:
        return 2
    elif x <= 29:
        return 3
    elif x <= 39:
        return 4
    elif x <= 49:
        return 5
    elif x <= 59:
        return 6
    elif x <= 69:
        return 7
    elif x <= 79:
        return 8
    elif x <= 89:
        return 9
    elif x <= 99:
        return 10
    elif x <= 109:
        return 11
    elif x <= 119:
        return 12
    elif x <= 129:
        return 13
    elif x <= 139:
        return 14
    else:
        return 999


df['num_lab_procedures'] = df['num_lab_procedures'].map(lab_proc_map)

print(df['num_lab_procedures'])

######## MEDICATIONS ########


def med_map(x):
    if x <= 9:
        return 1
    elif x <= 19:
        return 2
    elif x <= 29:
        return 3
    elif x <= 39:
        return 4
    elif x <= 49:
        return 5
    elif x <= 59:
        return 6
    elif x <= 69:
        return 7
    elif x <= 79:
        return 8
    elif x <= 89:
        return 9
    else:
        return 999


df['num_medications'] = df['num_medications'].map(med_map)

print(df['num_medications'])

######## OUTPATIENT ########


def outpt_map(x):
    if x <= 4:
        return 1
    elif x <= 9:
        return 2
    elif x <= 14:
        return 3
    elif x <= 19:
        return 4
    elif x <= 24:
        return 5
    elif x <= 29:
        return 6
    elif x <= 34:
        return 7
    elif x <= 39:
        return 8
    elif x <= 44:
        return 9
    else:
        return 999


df['number_outpatient'] = df['number_outpatient'].map(outpt_map)

print(df['number_outpatient'])


######## EMERGENCY ########

def emergency_map(x):
    if x <= 9:
        return 1
    elif x <= 19:
        return 2
    elif x <= 29:
        return 3
    elif x <= 39:
        return 4
    elif x <= 49:
        return 5
    elif x <= 59:
        return 6
    elif x <= 69:
        return 7
    elif x <= 79:
        return 8
    else:
        return 999


df['number_emergency'] = df['number_emergency'].map(emergency_map)

print(df['number_emergency'])

######## INPATIENT ########


def inpt_map(x):
    if x <= 4:
        return 1
    elif x <= 9:
        return 2
    elif x <= 14:
        return 3
    elif x <= 19:
        return 4
    elif x <= 24:
        return 5
    else:
        return 999


df['number_inpatient'] = df['number_inpatient'].map(inpt_map)

print(df['number_inpatient'])

######## DIAGNOSES ########


def diagn_map(x):
    if x
