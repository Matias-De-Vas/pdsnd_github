import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = ['january', 'february', 'march', 'april' , 'june', 'all']
days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'all']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    while True:
        try:
            city = input('Please, choose Chicago, Washington or New York City. ').lower()
            if city in CITY_DATA:
                print('Good choice!')
                break
            else:
                print('That\'s not a valid city')
        finally:
            print('(Value received)')
    
    while True:
        try:
            month = input('Please choose a month or type \'all\' for analyzing the whole year. ').lower()
            if month in months:
                print('Good choice!')
                break
            else:
                print('That\'s not a valid month')
        finally:
            print('(Value received)')
    
    while True:
        try:
            day = input('Please choose a day of the week (monday to friday) or type \'all\' for analyzing the whole week. ').lower()
            if day in days:
                print('Good choice!')
                break
            else:
                print('That\'s not a valid day')
        finally:
            print('(Value received)')

    print('-'*40)
    return city, month, day


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

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    most_common_month = df['month'].mode()[0]
    print('Most common month:', most_common_month)

    most_common_day = df['day_of_week'].mode()[0]
    print('Most common day of week:', most_common_day)

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    most_common_start_hour = df['hour'].mode()[0]
    print('Most common start hour:', most_common_start_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    most_common_start_station = df['Start Station'].mode()[0]
    print('Most common start station:', most_common_start_station)

    most_common_end_station = df['End Station'].mode()[0]
    print('Most common end station:', most_common_end_station)

    most_common_combination_station = (df['Start Station'] + ' / ' + df['End Station']).mode()[0]
    print('Most frequent combination of start and end stations:', most_common_combination_station)

    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time (seconds):', total_travel_time)

    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time (seconds):', mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    user_type_count = df['User Type'].value_counts()    
    print('Counts of user type:', user_type_count)
    
    try:
        gender_count = df['Gender'].value_counts()    
        print('Counts of gender:', gender_count)
    except:
        print('There\'s no Gender data for Washington')
   
    try:
        earliest_year_of_birth = df['Birth Year'].min()
        most_recent_year_of_birth = df['Birth Year'].max()
        most_common_year_of_birth = df['Birth Year'].mode()[0] 
        print('Earliest year of birth:', earliest_year_of_birth)
        print('Most recent year of birth:', most_recent_year_of_birth)
        print('Most common year of birth:', most_common_year_of_birth)
    except:
        print('There\'s no Birth Year data for Washington')
       
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def display_data(df):    
    view_data = input('Would you like to to see the first 5 rows of data? Enter yes or no. ').lower()
    start_loc = 0
    while view_data == 'yes':
        print(df.iloc[start_loc:start_loc + 5])
        start_loc += 5
        view_display = input('Do you wish to continue? Enter any key to continue or no to stop. ').lower()
        if view_display == 'no':
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
