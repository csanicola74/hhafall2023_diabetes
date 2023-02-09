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

###########################

########################
#### IMPORT DATASET ####
########################

# load in original dataset
df = pd.read_csv('data/2019-2020.csv')