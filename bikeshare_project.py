import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city =input('Please choose the name of the City(chicago,new york city,washington):').lower()
    while city not in CITY_DATA.keys():
        print('The city you have choosen is not reachable,Please choose a VALID city')
        city =input('Please choose the name of the City(chicago,new york city,washington):').lower()
    
    # TO DO: get user input for month (all, january, february, ... , june)
    months=['all','january','february','march','april','may','june']
    while True:
        month =input('Now enter the month(all,january,february,march,april,may,june):').lower()
        if month in months:
            break
        else:
            print('Something went wrong, maybe an invalid input.. Please try again with a VALID month')


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    AllDays=['all','monday','tuesday','wedensday','thursday','friday','saturday','sunday']
    while True:
        day =input('Please choose a weekday(all,monday,tuesday,wdensday,thursday,friday,saturday,sunday):').lower()
        if day in AllDays:
            return city, month, day
        else:
            print('Please try again with a correct weekday name')
            print('-'*40)


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
        """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['start_hour'] = df['Start Time'].dt.hour
    
    
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1
        df = df[df['month'] == month]
       
    if day != 'all':
        df = df[df['day_of_week']==day.title()]
        
    return df
    
        



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("The most common month:" ,df.loc[:,'month'].mode())


    # TO DO: display the most common day of week
    print("The most common day:" ,df.loc[:,'day_of_week'].mode())

    # TO DO: display the most common start hour
    print("The most common starting hour:" ,df.loc[:,'start_hour'].mode())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The most commonly used start station:",df.loc[:,'Start Station'].mode())


    # TO DO: display most commonly used end station
    print("The most commonly used End station:",df.loc[:,'End Station'].mode())


    # TO DO: display most frequent combination of start station and end station trip
    df['Combination'] = df['Start Station']+","+df['End Station']
    print("The most commonly used Combination :",df.loc[:,'Combination'].mode())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('the total duration of the trip:',df.loc[:,'Trip Duration'].sum())


    # TO DO: display mean travel time
    print('the average of the travel time:',df.loc[:,'Trip Duration'].mean())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('the number of user types:',df.loc[:,'User Type'].value_counts())


    # TO DO: Display counts of gender
    if 'Gender' in df:
        print('the counts of gender:',df.loc[:,'Gender'].value_counts())
        # TO DO: Display earliest, most recent, and most common year of birth
        print('the earliest Birth Year:',df.loc[:,'Birth Year'].min())
        print('the most common Birth Year:',df.loc[:,'Birth Year'].mean())
        print('the newest Birth Year:',df.loc[:,'Birth Year'].max())
        
        
    else:
        print('Gender stats cannot be calculated because Gender does not appear in the dataframe')
     


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(df):
    print('Raw data is ready to be checked')
    
    indexing=0 
    inputting=input('enter yes if you want to see 5 rows of Raw data ,and no if you dont').lower()
    if inputting not in ['yes','no']:
        print('your answer is not included')
        inputting=input('enter yes if you want to see 5 rows of Raw data ,and no if you dont').lower()
    elif inputting != 'yes':
        print('Thank You')
    else:
        while indexing+5 < df.shape[0]:
            print(df.iloc[indexing:indexing+5])
            indexing+=5
            inputting=input('do you wanna see 5 more?,enter yes or no').lower()
            if inputting != 'yes':
                print('Thank you')
                break
    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
