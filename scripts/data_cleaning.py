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

##########################
####  IMPORT DATASET  ####
##########################

# import the messy dataset
base_df = pd.read_csv(
    'data/diabetic_data_ORIGINAL.csv')
base_df.head()
base_df.shape
list(base_df.columns)


# USE THE BELOW CLEANING AS A REFERENCE
"""
#########################################
####  COMBINE SLEEP DATA TO DATASET  ####
#########################################
# read in sleep data
sleep = pd.read_csv('data/raw_data/Link_ID.csv')
sleep.info()
"""
"""
# join sleep data to main dataset on the MRN
df = base_df.join(
    sleep.set_index('MRN'), on='MRN', how='left')

df.dtypes

# reset the index
df = df.reset_index(drop=True)
df.dtypes

# save the merged dataset to a csv
df.to_csv('data/raw_data/StonyBrook_sleep_merge.csv', index=False)
# then load dataset back in
df = pd.read_csv('data/raw_data/StonyBrook_sleep_merge.csv')

#################################
####  CLEAN UP COLUMN NAMES  ####
#################################

# Creating a function which will remove extra leading
# and tailing whitespace from the data.
# pass dataframe as a parameter here


def whitespace_remover(dataframe):
    # iterating over the columns
    for i in dataframe.columns:
        # checking datatype of each columns
        if dataframe[i].dtype == 'object':
            # applying strip function on column
            dataframe[i] = dataframe[i].map(str.strip)
        else:
            # if condn. is False then it will do nothing.
            pass


# applying whitespace_remover function on dataframe
whitespace_remover(df)

# printing dataframe
print(df)

####  CLEAN UP COLUMN NAMES  ####

list(df.columns)
"""
['COHORT', 'QUESTIONNAIRE', 'MRN', 'FirstName', 'LastName', 'DOB', 'AgeToday', 'Gender',
 'Race', 'Ethnicity', 'SurveyCompletionDate', 'SurgeryType', 'LTF', 'PREOPBMI', 'ConsultWeight',
 'ConsultBMI', 'OVER1YEARPREOP', '@200365DAYSPREOP', '@100200DAYSPREOP', '@30100DAYSPREOP',
 '@030DAYSPREOP', 'DOS', '@030DAYSPOSTOP', '@30100DAYSPOSTOP', '@100200DAYSPOSTOP',
 '@200365DAYSPOSTOP', '@12YEARSPOSTOP', '@23YEARSPOSTOP', '@34YEARSPOSTOP', '@45YEARSPOSTOP',
 '@56YEARSPOSTOP', 'OVER6YEARSPOSTOP', 'TWL30100PRE030PO', 'TWL030PRE030PO', 'TWLPREOP30100DAYS',
 'TWLPREOP100200DAYS', 'TWLPREOP200365DAYS', 'TWLPREOP12YEARS', 'TWLPREOP23YEARS',
 'TWLPREOP34YEARS', 'TWLPREOP45YEARS', 'TWLPREOP56YEARS', 'TWLPREOPOVER6YEARS',
 'TFEQCOGNITIVERESTRAINT', 'TFEQEMOTIONALEATINGSCALE', 'TFEQUNRESTRAINEDEATING', 'YFASQ1',
 'YFASQ2', 'YFASQ3', 'YFASQ4', 'YFASQ5', 'YFASQ6', 'YFASQ7', 'YFASQ8', 'YFASTOTALMET',
 'BSIAttentionalImpulsiveness', 'BSIMotorImpulsiveness', 'BSINonplanningImpulsiveness',
 'BRIEFCOPESELFDISTRACTION', 'BRIEFCOPEACTIVECOPING', 'BRIEFCOPEDENIAL', 'BRIEFCOPESUBSTANCEUSE',
 'BRIEFCOPEUSEOFEMOTIONALSUPPORT', 'BRIEFCOPEUSEOFINSTRUMENTALSUPPORT',
 'BRIEFCOPEBEHAVIORALDISENGAGEMENT', 'BRIEFCOPEVENTING', 'BRIEFCOPEPOSITIVEREFRAMING',
 'BRIEFCOPEPLANNING', 'BRIEFCOPEHUMOR', 'BRIEFCOPEACCEPTANCE', 'BRIEFCOPERELIGION',
 'BRIEFCOPESELFBLAME', 'ISITotalScore', 'ISIScoreCategories', 'PSQIFIRSTANSWERTOTALS',
 'PSQISECONDANSWERTOTALS', 'Group', 'GRPSREQUIRED', 'GRPSATTENDED', 'Grp1_exerciselog',
 'Grp1_FitnessTracker', 'Grp1_typeofexercise', 'Grp1_frequency', 'Grp1_duration',
 'Grp1_Rateofperceivedexertion', 'Grp1_Intensityofexercise', 'Grp1_timesedentary',
 'Grp2_exerciselog', 'Grp2_FitnessTracker', 'Grp2_typeofexercise', 'Grp2_frequency',
 'Grp2_duration', 'Grp2_Rateofperceivedexertion', 'Grp2_Intensityofexercise',
 'Grp2_timesedentary', 'Grp3_exerciselog', 'Grp3_FitnessTracker', 'Grp3_typeofexercise',
 'Grp3_frequency', 'Grp3_duration', 'Grp3_Rateofperceivedexertion', 'Grp3_Intensityofexercise',
 'Grp3_timesedentary', 'Grp4_exerciselog', 'Grp4_FitnessTracker', 'Grp4_typeofexercise',
 'Grp4_frequency', 'Grp4_duration', 'Grp4_Rateofperceivedexertion', 'Grp4_Intensityofexercise',
 'Grp4_timesedentary', 'Grp5_exerciselog', 'Grp5_FitnessTracker', 'Grp5_typeofexercise',
 'Grp5_frequency', 'Grp5_duration', 'Grp5_Rateofperceivedexertion', 'Grp5_Intensityofexercise',
 'Grp5_timesedentary', 'V80', 'Grp6_exerciselog', 'Grp6_FitnessTracker', 'Grp6_typeofexercise',
 'Grp6_frequency', 'Grp6_duration', 'Grp6_Rateofperceivedexertion', 'Grp6_Intensityofexercise',
 'Grp6_timesedentary', 'Grp7_exerciselog', 'Grp7_FitnessTracker', 'Grp7_typeofexercise',
 'Grp7_frequency', 'Grp7_duration', 'Grp7_Rateofperceivedexertion', 'Grp7_Intensityofexercise',
 'Grp7_timesedentary', 'V95', 'Grp8_exerciselog', 'Grp8_FitnessTracker', 'Grp8_typeofexercise',
 'Grp8_frequency', 'Grp8_duration', 'Grp8_Rateofperceivedexertion', 'Grp8_Intensityofexercise',
 'Grp8_timesedentary', 'Grp9_exerciselog', 'Grp9_FitnessTracker', 'Grp9_typeofexercise',
 'Grp9_frequency', 'Grp9_duration', 'Grp9_Rateofperceivedexertion', 'Grp9_Intensityofexercise',
 'Grp9_timesedentary', 'Grp10_exerciselog', 'Grp10_FitnessTracker', 'Grp10_typeofexercise',
 'Grp10_frequency', 'Grp10_duration', 'Grp10_Rateofperceivedexertion', 'Grp10_Intensityofexercise',
 'Grp10_timesedentary', 'Grp11_exerciselog', 'Grp11_FitnessTracker', 'Grp11_typeofexercise',
 'Grp11_frequency', 'Grp11_duration', 'Grp11_Rateofperceivedexertion', 'Grp11_Intensityofexercise',
 'Grp11_timesedentary', 'Grp12_exerciselog', 'Grp12_FitnessTracker', 'Grp12_typeofexercise',
 'Grp12_frequency', 'Grp12_duration', 'Grp12_Rateofperceivedexertion', 'Grp12_Intensityofexercise',
 'Grp12_timesedentary', 'Grp13_exerciselog', 'Grp13_FitnessTracker', 'Grp13_typeofexercise',
 'Grp13_frequency', 'Grp13_duration', 'Grp13_Rateofperceivedexertion', 'Grp13_Intensityofexercise',
 'Grp13_timesedentary', 'Grp14_exerciselog', 'Grp14_FitnessTracker', 'Grp14_typeofexercise',
 'Grp14_frequency', 'Grp14_duration', 'Grp14_Rateofperceivedexertion', 'Grp14_Intensityofexercise',
 'Grp14_timesedentary', 'Grp15_exerciselog', 'Grp15_FitnessTracker', 'Grp15_typeofexercise',
 'Grp15_frequency', 'Grp15_duration', 'Grp15_Rateofperceivedexertion', 'Grp15_Intensityofexercise',
 'Grp15_timesedentary']
"""

df.dtypes


# convert all numeric columns from str to int
df['PREOPBMI'] = df['PREOPBMI'].replace(
    ' ', 0).replace('', 0).astype(float).astype(int)
df['ConsultWeight'] = df['ConsultWeight'].replace(
    ' ', 0).replace('', 0).astype(float).astype(int)
df['ConsultBMI'] = df['ConsultBMI'].replace(
    ' ', 0).replace('', 0).astype(float).astype(int)
df['OVER1YEARPREOP'] = df['OVER1YEARPREOP'].replace(
    ' ', 0).replace('', 0).astype(float).astype(int)
df['@200365DAYSPREOP'] = df['@200365DAYSPREOP'].replace(
    ' ', 0).replace('', 0).astype(float).astype(int)
df['@100200DAYSPREOP'] = df['@100200DAYSPREOP'].replace(
    ' ', 0).replace('', 0).astype(float).astype(int)
df['@30100DAYSPREOP'] = df['@30100DAYSPREOP'].replace(
    ' ', 0).replace('', 0).astype(float).astype(int)
df['@030DAYSPREOP'] = df['@030DAYSPREOP'].replace(
    ' ', 0).replace('', 0).astype(float).astype(int)
df['DOS'] = df['DOS'].replace(' ', 0).replace('', 0).astype(float).astype(int)
df['@030DAYSPOSTOP'] = df['@030DAYSPOSTOP'].replace(
    ' ', 0).replace('', 0).astype(float).astype(int)
df['@30100DAYSPOSTOP'] = df['@30100DAYSPOSTOP'].replace(
    ' ', 0).replace('', 0).astype(float).astype(int)
df['@100200DAYSPOSTOP'] = df['@100200DAYSPOSTOP'].replace(
    ' ', 0).replace('', 0).astype(float).astype(int)
df['@200365DAYSPOSTOP'] = df['@200365DAYSPOSTOP'].replace(
    ' ', 0).replace('', 0).astype(float).astype(int)
df['@12YEARSPOSTOP'] = df['@12YEARSPOSTOP'].replace(
    ' ', 0).replace('', 0).astype(float).astype(int)
df['@23YEARSPOSTOP'] = df['@23YEARSPOSTOP'].replace(
    ' ', 0).replace('', 0).astype(float).astype(int)
df['@34YEARSPOSTOP'] = df['@34YEARSPOSTOP'].replace(
    ' ', 0).replace('', 0).astype(float).astype(int)
df['@45YEARSPOSTOP'] = df['@45YEARSPOSTOP'].replace(
    ' ', 0).replace('', 0).astype(float).astype(int)
df['@56YEARSPOSTOP'] = df['@56YEARSPOSTOP'].replace(
    ' ', 0).replace('', 0).astype(float).astype(int)
df['OVER6YEARSPOSTOP'] = df['OVER6YEARSPOSTOP'].replace(
    ' ', 0).replace('', 0).astype(float).astype(int)

df.dtypes

# change date columns to datetime format
df['DOB'] = pd.to_datetime(df['DOB'], format='%Y/%m/%d')
df['SurveyCompletionDate'] = pd.to_datetime(
    df['SurveyCompletionDate'], format='%m/%d/%Y %H:%M')
print(df['SurveyCompletionDate'])


# rewrite 'AgeToday' column to calculate the age today from the DOB column
df['AgeToday'] = (pd.to_datetime('today') - df['DOB']).astype('<m8[Y]')
print(df['AgeToday'])

# adding age group column


def age_group(df):
    if df['AgeToday'] <= 18:
        return '0-18'
    elif df['AgeToday'] <= 25:
        return '19-25'
    elif df['AgeToday'] <= 35:
        return '26-35'
    elif df['AgeToday'] <= 45:
        return '36-45'
    elif df['AgeToday'] <= 55:
        return '46-55'
    elif df['AgeToday'] <= 65:
        return '56-65'
    elif df['AgeToday'] <= 75:
        return '66-75'
    elif df['AgeToday'] <= 85:
        return '76-85'
    elif df['AgeToday'] <= 95:
        return '86-95'
    elif df['AgeToday'] <= 105:
        return '96-105'
    else:
        return 'unknown'


df['AgeGroup'] = df.apply(age_group, axis=1)

########################################
####  OVERWRITE CALCULATED COLUMNS  ####
########################################


# total weight loss 30 - 100 days pre-op to 0 - 30 days pre-op


def TWL30100PRE030PO(df):
    if (df['@30100DAYSPREOP'] > 0) & (df['@030DAYSPREOP'] > 0):
        return df['@030DAYSPREOP'] / df['@30100DAYSPREOP']


df['TWL30100PRE030PO'] = df.apply(TWL30100PRE030PO, axis=1)

# total weight loss 0 - 30 days pre-op to 0 - 30 days post-op


def TWL030PRE030PO(df):
    if (df['@030DAYSPREOP'] > 0) & (df['@030DAYSPOSTOP'] > 0):
        return df['@030DAYSPOSTOP'] / df['@030DAYSPREOP']


df['TWL030PRE030PO'] = df.apply(TWL030PRE030PO, axis=1)

# total weight loss pre-op to 30 - 100 days post-op


def TWLPREOP30100DAYS(df):
    if (df['@30100DAYSPOSTOP'] > 0) & (df['@030DAYSPREOP'] > 0):
        return df['@30100DAYSPOSTOP'] / df['@030DAYSPREOP']


df['TWLPREOP30100DAYS'] = df.apply(TWLPREOP30100DAYS, axis=1)

# total weight loss pre-op to 100 - 200 days post-op


def TWLPREOP100200DAYS(df):
    if (df['@100200DAYSPOSTOP'] > 0) & (df['@030DAYSPREOP'] > 0):
        return df['@100200DAYSPOSTOP'] / df['@030DAYSPREOP']


df['TWLPREOP100200DAYS'] = df.apply(TWLPREOP100200DAYS, axis=1)

# total weight loss pre-op to 200 - 365 days post-op


def TWLPREOP100200DAYS(df):
    if (df['@200365DAYSPOSTOP'] > 0) & (df['@030DAYSPREOP'] > 0):
        return df['@200365DAYSPOSTOP'] / df['@030DAYSPREOP']


df['TWLPREOP100200DAYS'] = df.apply(TWLPREOP100200DAYS, axis=1)

# total weight loss pre-op to 1 - 2 years post-op


def TWLPREOP12YEARS(df):
    if (df['@12YEARSPOSTOP'] > 0) & (df['@030DAYSPREOP'] > 0):
        return df['@12YEARSPOSTOP'] / df['@030DAYSPREOP']


df['TWLPREOP12YEARS'] = df.apply(TWLPREOP12YEARS, axis=1)

# total weight loss pre-op to 2 - 3 years post-op


def TWLPREOP23YEARS(df):
    if (df['@23YEARSPOSTOP'] > 0) & (df['@030DAYSPREOP'] > 0):
        return df['@23YEARSPOSTOP'] / df['@030DAYSPREOP']


df['TWLPREOP23YEARS'] = df.apply(TWLPREOP23YEARS, axis=1)

# total weight loss pre-op to 3 - 4 years post-op


def TWLPREOP34YEARS(df):
    if (df['@34YEARSPOSTOP'] > 0) & (df['@030DAYSPREOP'] > 0):
        return df['@34YEARSPOSTOP'] / df['@030DAYSPREOP']


df['TWLPREOP34YEARS'] = df.apply(TWLPREOP34YEARS, axis=1)

# total weight loss pre-op to 4 - 5 years post-op


def TWLPREOP45YEARS(df):
    if (df['@45YEARSPOSTOP'] > 0) & (df['@030DAYSPREOP'] > 0):
        return df['@45YEARSPOSTOP'] / df['@030DAYSPREOP']


df['TWLPREOP45YEARS'] = df.apply(TWLPREOP45YEARS, axis=1)

# total weight loss pre-op to 5 - 6 years post-op


def TWLPREOP56YEARS(df):
    if (df['@56YEARSPOSTOP'] > 0) & (df['@030DAYSPREOP'] > 0):
        return df['@56YEARSPOSTOP'] / df['@030DAYSPREOP']


df['TWLPREOP56YEARS'] = df.apply(TWLPREOP56YEARS, axis=1)

# total weight loss pre-op to over 6 years post-op


def TWLPREOPOVER6YEARS(df):
    if (df['OVER6YEARSPOSTOP'] > 0) & (df['@030DAYSPREOP'] > 0):
        return df['OVER6YEARSPOSTOP'] / df['@030DAYSPREOP']


df['TWLPREOPOVER6YEARS'] = df.apply(TWLPREOPOVER6YEARS, axis=1)

#####################################################
####  CONVERT QUESTIONNAIRE COLUMNS TO INTEGERS  ####
#####################################################

# convert all numeric columns from str to int
df['TFEQCOGNITIVERESTRAINT'] = df['TFEQCOGNITIVERESTRAINT'].replace(
    ' ', 0).replace('', 0).astype(float).astype(int)

df['TFEQEMOTIONALEATINGSCALE'] = df['TFEQEMOTIONALEATINGSCALE'].replace(
    ' ', 0).replace('', 0).astype(float).astype(int)

df['TFEQUNRESTRAINEDEATING'] = df['TFEQUNRESTRAINEDEATING'].replace(
    ' ', 0).replace('', 0).astype(float).astype(int)

df['YFASQ1'] = df['YFASQ1'].replace(
    ' ', 0).replace('', 0).astype(float).astype(int)

df['YFASQ2'] = df['YFASQ2'].replace(
    ' ', 0).replace('', 0).astype(float).astype(int)

df['YFASQ3'] = df['YFASQ3'].replace(
    ' ', 0).replace('', 0).astype(float).astype(int)

df['YFASQ4'] = df['YFASQ4'].replace(
    ' ', 0).replace('', 0).astype(float).astype(int)

df['YFASQ5'] = df['YFASQ5'].replace(
    ' ', 0).replace('', 0).astype(float).astype(int)

df['YFASQ6'] = df['YFASQ6'].replace(
    ' ', 0).replace('', 0).astype(float).astype(int)

df['YFASQ7'] = df['YFASQ7'].replace(
    ' ', 0).replace('', 0).astype(float).astype(int)

df['YFASQ8'] = df['YFASQ8'].replace(
    ' ', 0).replace('', 0).astype(float).astype(int)

df['YFASTOTALMET'] = df['YFASTOTALMET'].replace(
    ' ', 0).replace('', 0).astype(float).astype(int)

df['BSIAttentionalImpulsiveness'] = df['BSIAttentionalImpulsiveness'].replace(
    ' ', 0).replace('', 0).astype(float).astype(int)

df['BSIMotorImpulsiveness'] = df['BSIMotorImpulsiveness'].replace(
    ' ', 0).replace('', 0).astype(float).astype(int)

df['BSINonplanningImpulsiveness'] = df['BSINonplanningImpulsiveness'].replace(
    ' ', 0).replace('', 0).astype(float).astype(int)

df['BRIEFCOPESELFDISTRACTION'] = df['BRIEFCOPESELFDISTRACTION'].replace(
    ' ', 0).replace('', 0).astype(float).astype(int)

df['BRIEFCOPEACTIVECOPING'] = df['BRIEFCOPEACTIVECOPING'].replace(
    ' ', 0).replace('', 0).astype(float).astype(int)

df['BRIEFCOPEDENIAL'] = df['BRIEFCOPEDENIAL'].replace(
    ' ', 0).replace('', 0).astype(float).astype(int)

df['BRIEFCOPESUBSTANCEUSE'] = df['BRIEFCOPESUBSTANCEUSE'].replace(
    ' ', 0).replace('', 0).astype(float).astype(int)

df['BRIEFCOPEUSEOFEMOTIONALSUPPORT'] = df['BRIEFCOPEUSEOFEMOTIONALSUPPORT'].replace(
    ' ', 0).replace('', 0).astype(float).astype(int)

df['BRIEFCOPEUSEOFINSTRUMENTALSUPPORT'] = df['BRIEFCOPEUSEOFINSTRUMENTALSUPPORT'].replace(
    ' ', 0).replace('', 0).astype(float).astype(int)

df['BRIEFCOPEBEHAVIORALDISENGAGEMENT'] = df['BRIEFCOPEBEHAVIORALDISENGAGEMENT'].replace(
    ' ', 0).replace('', 0).astype(float).astype(int)

df['BRIEFCOPEVENTING'] = df['BRIEFCOPEVENTING'].replace(
    ' ', 0).replace('', 0).astype(float).astype(int)

df['BRIEFCOPEPOSITIVEREFRAMING'] = df['BRIEFCOPEPOSITIVEREFRAMING'].replace(
    ' ', 0).replace('', 0).astype(float).astype(int)

df['BRIEFCOPEPLANNING'] = df['BRIEFCOPEPLANNING'].replace(
    ' ', 0).replace('', 0).astype(float).astype(int)

df['BRIEFCOPEHUMOR'] = df['BRIEFCOPEHUMOR'].replace(
    ' ', 0).replace('', 0).astype(float).astype(int)

df['BRIEFCOPEACCEPTANCE'] = df['BRIEFCOPEACCEPTANCE'].replace(
    ' ', 0).replace('', 0).astype(float).astype(int)

df['BRIEFCOPERELIGION'] = df['BRIEFCOPERELIGION'].replace(
    ' ', 0).replace('', 0).astype(float).astype(int)

df['BRIEFCOPESELFBLAME'] = df['BRIEFCOPESELFBLAME'].replace(
    ' ', 0).replace('', 0).astype(float).astype(int)

df['ISITotalScore'] = df['ISITotalScore'].replace(
    ' ', 0).replace('', 0).astype(float).astype(int)

df['PSQIFIRSTANSWERTOTALS'] = df['PSQIFIRSTANSWERTOTALS'].replace(
    ' ', 0).replace('', 0).astype(float).astype(int)

df['PSQISECONDANSWERTOTALS'] = df['PSQISECONDANSWERTOTALS'].replace(
    ' ', 0).replace('', 0).astype(float).astype(int)

############################
#### CONVERT GROUP DATA ####
############################

df['Group'] = df['Group'].replace(
    ' ', 0).replace('', 0).astype(float).astype(int)

df['GRPSREQUIRED'] = df['GRPSREQUIRED'].replace(
    ' ', 0).replace('', 0).astype(float).astype(int)

df['GRPSATTENDED'] = df['GRPSATTENDED'].replace(
    ' ', 0).replace('', 0).astype(float).astype(int)

list(df.columns)
# drop group data for this project
df = df.drop(columns=['Group', 'GRPSREQUIRED', 'GRPSATTENDED', 'Grp1_exerciselog', 'Grp1_FitnessTracker', 'Grp1_typeofexercise', 'Grp1_frequency', 'Grp1_duration', 'Grp1_Rateofperceivedexertion', 'Grp1_Intensityofexercise', 'Grp1_timesedentary', 'Grp2_exerciselog', 'Grp2_FitnessTracker', 'Grp2_typeofexercise', 'Grp2_frequency', 'Grp2_duration', 'Grp2_Rateofperceivedexertion', 'Grp2_Intensityofexercise', 'Grp2_timesedentary', 'Grp3_exerciselog', 'Grp3_FitnessTracker', 'Grp3_typeofexercise', 'Grp3_frequency', 'Grp3_duration', 'Grp3_Rateofperceivedexertion', 'Grp3_Intensityofexercise', 'Grp3_timesedentary', 'Grp4_exerciselog', 'Grp4_FitnessTracker', 'Grp4_typeofexercise', 'Grp4_frequency', 'Grp4_duration', 'Grp4_Rateofperceivedexertion', 'Grp4_Intensityofexercise', 'Grp4_timesedentary', 'Grp5_exerciselog', 'Grp5_FitnessTracker', 'Grp5_typeofexercise', 'Grp5_frequency', 'Grp5_duration', 'Grp5_Rateofperceivedexertion', 'Grp5_Intensityofexercise', 'Grp5_timesedentary', 'V80', 'Grp6_exerciselog', 'Grp6_FitnessTracker', 'Grp6_typeofexercise', 'Grp6_frequency', 'Grp6_duration', 'Grp6_Rateofperceivedexertion', 'Grp6_Intensityofexercise', 'Grp6_timesedentary', 'Grp7_exerciselog', 'Grp7_FitnessTracker', 'Grp7_typeofexercise', 'Grp7_frequency', 'Grp7_duration', 'Grp7_Rateofperceivedexertion', 'Grp7_Intensityofexercise', 'Grp7_timesedentary', 'V95', 'Grp8_exerciselog', 'Grp8_FitnessTracker', 'Grp8_typeofexercise', 'Grp8_frequency',
             'Grp8_duration', 'Grp8_Rateofperceivedexertion', 'Grp8_Intensityofexercise', 'Grp8_timesedentary', 'Grp9_exerciselog', 'Grp9_FitnessTracker', 'Grp9_typeofexercise', 'Grp9_frequency', 'Grp9_duration', 'Grp9_Rateofperceivedexertion', 'Grp9_Intensityofexercise', 'Grp9_timesedentary', 'Grp10_exerciselog', 'Grp10_FitnessTracker', 'Grp10_typeofexercise', 'Grp10_frequency', 'Grp10_duration', 'Grp10_Rateofperceivedexertion', 'Grp10_Intensityofexercise', 'Grp10_timesedentary', 'Grp11_exerciselog', 'Grp11_FitnessTracker', 'Grp11_typeofexercise', 'Grp11_frequency', 'Grp11_duration', 'Grp11_Rateofperceivedexertion', 'Grp11_Intensityofexercise', 'Grp11_timesedentary', 'Grp12_exerciselog', 'Grp12_FitnessTracker', 'Grp12_typeofexercise', 'Grp12_frequency', 'Grp12_duration', 'Grp12_Rateofperceivedexertion', 'Grp12_Intensityofexercise', 'Grp12_timesedentary', 'Grp13_exerciselog', 'Grp13_FitnessTracker', 'Grp13_typeofexercise', 'Grp13_frequency', 'Grp13_duration', 'Grp13_Rateofperceivedexertion', 'Grp13_Intensityofexercise', 'Grp13_timesedentary', 'Grp14_exerciselog', 'Grp14_FitnessTracker', 'Grp14_typeofexercise', 'Grp14_frequency', 'Grp14_duration', 'Grp14_Rateofperceivedexertion', 'Grp14_Intensityofexercise', 'Grp14_timesedentary', 'Grp15_exerciselog', 'Grp15_FitnessTracker', 'Grp15_typeofexercise', 'Grp15_frequency', 'Grp15_duration', 'Grp15_Rateofperceivedexertion', 'Grp15_Intensityofexercise', 'Grp15_timesedentary'])

#############################################
####  CONVERT SLEEP COLUMNS TO INTEGERS  ####
#############################################

# fill sleep columns in with 999 and convert to integers
df['Epworth_Reading'] = df['Epworth_Reading'].fillna(999).astype(int)
df['Epworth_Watching'] = df['Epworth_Watching'].fillna(999).astype(int)
df['Epworth_Sitting'] = df['Epworth_Sitting'].fillna(999).astype(int)
df['Epworth_Passenger'] = df['Epworth_Passenger'].fillna(999).astype(int)
df['Epworth_Lying'] = df['Epworth_Lying'].fillna(999).astype(int)
df['Epworth_Talking'] = df['Epworth_Talking'].fillna(999).astype(int)
df['Epworth_Lunch'] = df['Epworth_Lunch'].fillna(999).astype(int)
df['Epworth_Car'] = df['Epworth_Car'].fillna(999).astype(int)
df['STOPBang_Snoring'] = df['STOPBang_Snoring'].fillna(999).astype(int)
df['STOPBang_Tired'] = df['STOPBang_Tired'].fillna(999).astype(int)
df['STOPBang_Observed'] = df['STOPBang_Observed'].fillna(999).astype(int)
df['STOPBang_BloodPressure'] = df['STOPBang_BloodPressure'].fillna(
    999).astype(int)
df['STOPBang_BMI'] = df['STOPBang_BMI'].fillna(999).astype(int)
df['STOPBang_Age'] = df['STOPBang_Age'].fillna(999).astype(int)
df['STOPBang_NeckCircumference'] = df['STOPBang_NeckCircumference'].fillna(
    999).astype(int)
df['STOPBang_Gender'] = df['STOPBang_Gender'].fillna(999).astype(int)

################################################
####  DROP ALL PATIENT IDENTIFYING COLUMNS  ####
################################################

df = df.drop(columns=['MRN', 'FirstName', 'LastName', 'DOB'])

# drop columns don't need
df = df.drop(columns=['LTF'])
df.info()
df.dtypes
################################
####  SAVE DATAFRAME TO CSV ####
################################

df.to_csv('data/clean_data/StonyBrook_CLEAN.csv', index=False)

"""
