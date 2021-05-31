import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
pd.set_option('display.max_columns', None)
pd.read_csv(r'C:\Users\Inez\Documents\IntroRepo\Hotel Booking Data\hotel_bookings.csv')
hotel_bookings = pd.read_csv(r'C:\Users\Inez\Documents\IntroRepo\Hotel Booking Data\hotel_bookings.csv')

hotel_bookings.describe()
len(hotel_bookings)
hotel_bookings.info
hotel_bookings.shape
hotel_bookings.dtypes
hotel_bookings.index
hotel_bookings.values
hotel_bookings.columns
hotel_bookings.index
hotel_bookings.head()
hotel_bookings.isnull().sum().sort_values(ascending=False)[:10]
len(hotel_bookings)
hotel_bookings.isnull().sum()
#all good ways to explore the file to get a look at the data

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

## If no id of agent or company is null, just replace it with 0
hotel_bookings[['agent','company']] = hotel_bookings[['agent','company']].fillna(0.0)
len(hotel_bookings)

hotel_bookings[(hotel_bookings.adults+hotel_bookings.babies+hotel_bookings.children)==0].shape

## Drop Rows where there is no adult, baby and child
hotel_bookings = hotel_bookings.drop(hotel_bookings[(hotel_bookings.adults+hotel_bookings.babies+hotel_bookings.children)==0].index)

hotel_bookings[(hotel_bookings.adults+hotel_bookings.babies+hotel_bookings.children)==0].shape

## for missing children value, replace it with rounded mean value

## note working ...hotel_bookings[['children', 'company']] = hotel_bookings[['children', 'company']].astype('int64')
##not working hotel_bookings[['children', 'company', 'agent']] = hotel_bookings[['children', 'company', 'agent']].astype('int64')
hotel_bookings[['hotel']]
hotel_bookings[['market_segment']]
hotel_bookings[['distribution_channel']]
columns = ['market_segment', 'meal', 'customer_type']
hotel_bookings[columns]

##to run some analysis on the data
hotel_bookings.groupby(['arrival_date_week_number']).count()['hotel'].sort_values(ascending=False)
hotel_bookings.groupby(['customer_type']).count()['hotel'].sort_values(ascending=False)
hotel_bookings.groupby(['reservation_status']).count()['hotel'].sort_values(ascending=False)
hotel_bookings.groupby(['meal']).count()['hotel'].sort_values(ascending=False)
hotel_bookings.groupby(['arrival_date_month']).count()['hotel'].sort_values(ascending=False)

##How Many Booking Were Cancelled?
is_can = len(hotel_bookings[hotel_bookings['is_canceled']==1])
print("Percentage cancelation= ", is_can/len(hotel_bookings))
hotel_bookings['reservation_status'].value_counts(normalize=True)*100

corr= hotel_bookings.corr(method='pearson')['is_canceled'][:]
corr
#showa the highest positive correlations

resort_canceled = hotel_bookings[(hotel_bookings['hotel']=='Resort Hotel') & (hotel_bookings['is_canceled']==1)]
city_canceled = hotel_bookings[(hotel_bookings['hotel']=='City Hotel') & (hotel_bookings['is_canceled']==1)]

print('Cancelations in resort hotel= ', (len(resort_canceled))/(len(hotel_bookings[hotel_bookings['hotel']=='Resort Hotel'])))
print('Cancelations in city hotel= ', (len(city_canceled))/(len(hotel_bookings[hotel_bookings['hotel']=='City Hotel'])))

##Cancelations in resort hotel=  0.27975047984644913
##Cancelations in city hotel=  0.41711850301364334
#Our City hotels have higher cancelation rate than resort hotels, is valid.

grid = sns.FacetGrid(hotel_bookings, col='is_canceled')
grid.map(plt.hist, 'lead_time', width=50)
grid.add_legend()

print(len(hotel_bookings[(hotel_bookings['stays_in_weekend_nights']==0) & (hotel_bookings['stays_in_week_nights']==0)])) 
##701 bookings don't have both weekday or weekend nights which could be ar error in the data as this is not possible in real life scenario. Therefore these rows can be eliminated from the dataset.

((len(hotel_bookings.loc[(hotel_bookings['children']!=0) | (hotel_bookings['babies']!=0)]))/(len(hotel_bookings))) * 100

#Number of bookings that have children or babies/both is only 7.84% of the total population - ignore as not significant in deciding whether to cancel the booking or not. 


sns.countplot(data=hotel_bookings, x='previous_cancellations', hue='is_canceled')
#Majority of bookings have no previous cancellations, therefore less likely to cancel..but #
#bookings that have perviousy been cancelled once earlier are more likely to cancel again
sns.countplot(data=hotel_bookings, x='is_repeated_guest', hue='is_canceled')
new_guest = hotel_bookings[(hotel_bookings['is_repeated_guest']==0) & (hotel_bookings['is_canceled']==1)]
old_guest = hotel_bookings[(hotel_bookings['is_repeated_guest']==1) & (hotel_bookings['is_canceled']==1)]
print('Cancelations among new guests= ', (len(new_guest))/(len(hotel_bookings[hotel_bookings['is_repeated_guest']==0])))
print('Cancelations among old guests= ', (len(old_guest))/(len(hotel_bookings[hotel_bookings['is_repeated_guest']==1])))

##Table shows that majority of customers are new and they are less less likely to cancel booking.
## Old guests are less likely to cancel the booking (14.5%)

temp = hotel_bookings.loc[hotel_bookings['reserved_room_type']!=hotel_bookings['assigned_room_type']]
temp['is_canceled'].value_counts(normalize=True)*100

sns.pointplot(data=hotel_bookings, x='booking_changes', y='is_canceled')

# is there a trend of cancellations when the room type is different? No evidence 

chart = sns.catplot(data=hotel_bookings, x='arrival_date_month', hue='is_canceled', kind='count')
chart.set_xticklabels(rotation=65, horizontalalignment='right')

#Maximum bookings July and August (2016)

year_count = hotel_bookings.groupby(['arrival_date_year', 'is_canceled']).size().to_frame(name='count')
year_perct = year_count.groupby(level=0).apply(lambda x:100 * x / float(x.sum()))
print(year_perct)

month_count = hotel_bookings.groupby(['arrival_date_month', 'is_canceled']).size().to_frame(name='count')
month_perct = month_count.groupby(level=0).apply(lambda x:100 * x / float(x.sum()))
print(month_perct)

##% of cancellations higher in 2015 and 2017 even though bookings are higher in 2016.
 #April and June are the highest months for cancellations
 
print(hotel_bookings['customer_type'].value_counts(normalize=True)*100)
sns.countplot(data=hotel_bookings, x='customer_type', hue='is_canceled')
 
#75% bookings occur in Transient customers (walk in etc - may be a good target marketing strategy.
#This category also has the highest cancellation rate

hotel_bookings['reservation_status'].unique()

grid = sns.FacetGrid(hotel_bookings, col='arrival_date_year')
grid.map(sns.countplot, 'hotel')


hotel_bookings['meal'].nunique(), hotel_bookings['customer_type'].nunique()
grid = sns.FacetGrid(hotel_bookings, col='customer_type')
grid.map(sns.countplot, 'meal')
#Accross the board BB is the most booked option (again used in marketing).

hotel_bookings.pivot_table(columns='hotel', values='country', aggfunc=lambda x:x.mode())
##looking at country code PRT /Portugal has the higher number of bokkings (compared to other Countrys)

print(hotel_bookings.groupby(['customer_type', 'deposit_type']).size())

#Each category of customers book hotels without deposit.Lookings at refundable/non-refundable type
##ther are higher number of people book hotels that are non-refundable (may be last minute deals marketing)

print(hotel_bookings.groupby(['hotel', 'distribution_channel']).size())
print("-"*40)
print(hotel_bookings.groupby(['hotel', 'market_segment']).size())

#Looking at this data we can analysis the relationship between frequent customer types at each hotel and type of booking - Again this data is invaluable for marketing strategies

ccode = (pd.read_csv(r'C:\Users\Inez\Documents\IntroRepo\Hotel Booking Data\iso-country-codes.csv'))
hotel_bookings.merge(ccode, left_on ='country', right_on='Country')
# Importing CSV file into Pandas DataFrame data downloaded from Kaggle


https://www..in/Hotel_Review-g1162480-d478012-Reviews-Radisson_BLU_Resort_Temple_Bay_Mamallapuram-Mahabalipuram_Kanchipuram_District_Tamil_N.html

import plotly.express as px
#Customer Nationality Distribution
df5=pd.DataFrame({'Total customers':hotel_bookings['country'].value_counts()})
px.choropleth(df5,
        locations=df5.index,
        color='Total customers',
        hover_name='Total customers',
        color_continuous_scale=px.colors.sequential.Plasma,
        title="guest Department").show()
print(df5)
