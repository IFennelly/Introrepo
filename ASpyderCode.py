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
#Note not dropping any line from the datacheck above as duplicat countries/agents 
##and companies are all valid duplications

hotel_bookings['country'].isnull().sum() / len(hotel_bookings)
##.004% of "Country" data is null
hotel_bookings.dropna(axis=0, how='all', subset=['country'])

hotel_bookings[0:20]

hotel_bookings[0:20][['distribution_channel']]

columns = ['market_segment', 'meal', 'customer_type']
hotel_bookings[columns]

repeat_guests_cancel = (hotel_bookings['is_repeated_guest'] > 0) & (hotel_bookings['previous_cancellations'] > 0)
print(repeat_guests_cancel)
#hotel_bookings(repeat_guests_cancel)  QUERY NOT WORKING

import requests
iss = requests.get(' forecasts	http://www.7timer.info/bin/api.pl?')

country_map = gpd.read_file('counties.geojson')
country_map.plot()
country_map.crs
###TRY AND MERGE
Merge vaccine data with population data
cv_pop = pd.merge(cv_df_grp, pop_2019, on="Country Code")
#  Add a column to get vaccines per capita
cv_pop["Vac_per_Capita"] = cv_pop["Daily_Sum"] / cv_pop["Population"]


####ADD A PHOTO??
#from PIL import Image
#myImage = Image.open("your_image_here");
#myImage.show();

##To merge two files in python, you have to ask from user to enter name of the first
## and second file, and then ask a file name to create a file to place the merged content of the two file into this newly created file.
import pandas as pd
ccode = [pd.read_csv(r'C:\Users\Inez\Documents\IntroRepo\Hotel Booking Data\iso-country-codes.csv')]
df = pd.concat(ccode)
hotel_bookings.merge(ccode, right on 'English short name lower case')