# Various data prep techniques

# dataframe name customers
import pandas as pd

cust = pd.DataFrame({'Income': ['$1,200', '$2,500', '$3,750']})

cust['Income'] = cust.Income.str.replace('$', '').str.repalce(',', '')
cust['Income'] = pd.to_numeric(cust['Income'])
cust.info()  # to verify changes

# change floats to ints - more memory efficient
cust['Income'] = cust['Income'].astype('int')
cust.info()  # to verify changes

# change object to datetime
cust = pd.DataFrame({'DOB': ['01-15-1990', '06-30-1985', '12-05-2000']})
cust['DOB'] = pd.to_datetime(cust['DOB'], format='%m/-%d/-%y')
cust.info()  # to verify changes

# Extract date time elements
cust['Year'] = cust['DOB'].dt.year
cust['Month'] = cust['DOB'].dt.month
cust['Day'] = cust['DOB'].dt.day
cust['DayofWeek'] = cust['DOB'].dt.dayofweek

# Drop DOB column
cust = cust.drop(columns=['DOB'])
cust.info()  # to verify changes

# need bin date time elements
bins = [0, 1980, 1990, 2000, 2010]
labels = ['Before 80s', '80s', '90s', '2000s']
cust['DOB_Binned'] = pd.cut(cust['Year'], bins=bins, labels=labels)
cust.info()  # to verify changes


# np.where to convert yes/no column to 1 and 0
# Can be used on various binary columns with adjustments
'''
customers['Discount'] = np.where(customers['Discount'] == 'Yes', 1, 0)

'''

# Dummy Variables - Categorical to numeric
'''
dummies_edu = pd.get_dummies(customers['Education Level']).astype(int).drop_first=True

# Combine tables
customers = pd.concat([customers, dunniues_edu], axis=1)

# drop educations field
customers = customers.drop(columns=['Education Level'])

'''
