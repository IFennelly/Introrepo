
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
pd.read_csv(r'C:\Users\Inez\Documents\IntroRepo\Hotel Booking Data\hotel_bookings.csv')
hotel_bookings = pd.read_csv(r'C:\Users\Inez\Documents\IntroRepo\Hotel Booking Data\hotel_bookings.csv')
# Importing CSV file into Pandas DataFrame data downloaded from Kaggle

hotel_bookings.describe()
hotel_bookings.info
hotel_bookings.shape
hotel_bookings.dtypes
hotel_bookings.index
hotel_bookings.values
hotel_bookings.columns
hotel_bookings.index
hotel_bookings.head()
#all good ways to explore the file to get a look at the data
len(hotel_bookings)
hotel_bookings.isnull().sum()

#Dropping duplicates
#hotel_bookings.drop_duplicates(subset=['University'])
hotel_bookings.sort_values('country', ascending=False)
def checkIfDuplicates_1(hotel_bookings):
    ''' Check if given list contains any duplicates '''
    if len(hotel_bookings) == len(set(hotel_bookings)):
        return False
    else:
        return True
result = checkIfDuplicates_1(hotel_bookings)
if result:
    print('Yes, list contains duplicates')
else:
    print('No duplicates found in list')  
    
duplicates = hotel_bookings.duplicated()
hotel_bookings[duplicates]

hotel_bookings.dropna(axis=0, how='all', subset=['country'], inplace=True)
#Dropping of NA data 

hotel_bookings['country'].isnull().sum() / len(hotel_bookings)
##.004% of "Country" data is null
hotel_bookings.dropna(axis=0, how='all', subset=['country'])
hotel_bookings.dropna(axis=0, how='all', subset=['country'], inplace=True)

hotel_bookings[0:20]

hotel_bookings[0:20][['distribution_channel']]

columns = ['market_segment', 'meal', 'customer_type']
hotel_bookings[columns]

repeat_guests_cancel = (hotel_bookings['is_repeated_guest'] > 0) & (hotel_bookings['previous_cancellations'] > 0)
print(repeat_guests_cancel)

##to run some analysis on the data
hotel_bookings.groupby(['arrival_date_week_number']).count()['hotel'].sort_values(ascending=False)
hotel_bookings.groupby(['customer_type']).count()['hotel'].sort_values(ascending=False)
hotel_bookings.groupby(['reservation_status']).count()['hotel'].sort_values(ascending=False)
hotel_bookings.groupby(['meal']).count()['hotel'].sort_values(ascending=False)
hotel_bookings.groupby(['arrival_date_month']).count()['hotel'].sort_values(ascending=False)

# Importing CSV file into Pandas DataFrame data downloaded from Kaggle
ccode = (pd.read_csv(r'C:\Users\Inez\Documents\IntroRepo\Hotel Booking Data\iso-country-codes.csv'))
hotel_bookings.merge(ccode, left_on ='country', right_on='Country Name')

