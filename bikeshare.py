import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTHS = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
DAYS = ['all', 'sunday','monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']

def getCity():
    """
    Asks user to specify a city to analyze.

    Returns:
        (str) city - name of the city to analyze
    """
    while True :
        city = input('Would you like to see data for chicago, new york city, washington ?')
        if(city.lower() not in CITY_DATA):
            print('You did not enter a valid City, valid cities are {}. Let\'s try again.'.format(list(CITY_DATA.keys())))
            continue
        break
    return city.lower()


def getMonth():
    """
    Asks user to specify a monthto analyze.

    Returns:
        (str) month - name of the month to filter by, or "all" to apply no month filter
    """
    while True :
        month = input('Which month - January, February, March, April, May, June or All?')
        if(month.lower() not in MONTHS):
            print('You did not enter a valid Month.valid months are {}. Let\'s try again.'.format(MONTHS))
            continue
        break
    return month.lower()

def getDayOfWeek():
    """
    Asks user to specify a day to analyze.

    Returns:
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    while True :
        day = input('Which day? (all, monday, tuesday, ... sunday)')
        if(day.lower() not in DAYS):
            print('You did not enter a valid Day.valid day {}. Let\'s try again.'.format(DAYS))
            continue
        break
    return day.lower()

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = getCity()

    while True:
        option = input(
            'Would you like filter the data by month,day, both, or not at all ? Type "none" for no time filter.')
        options = ['month', 'day', 'both', 'none']
        if (option.lower() not in options):
            print('You did not enter a valid Option. valid options {}. Let\'s try again.'.format(options))
            continue
        option = option.lower()
        break

    if (option == 'month'): # get user input for month (all, january, february, ... , june)
        month = getMonth()
        day = 'all'
    elif (option == 'day'): # get user input for day of week (all, monday, tuesday, ... sunday)
        day = getDayOfWeek()
        month = 'all'
    elif (option == 'both'):
        month = getMonth()
        day = getDayOfWeek()
    else:
        month = 'all'
        day = 'all'

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
    # Load data from file to dataframe
    fileName = "dataset/{}".format(CITY_DATA[city])
    df = pd.read_csv(fileName)

    # convert the Start Time column to datetime to extract month and day of week
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        month_index = MONTHS.index(month)
        # filter by month to create the new dataframe
        df = df[df['month'] == month_index]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month


    # display the most common day of week


    # display the most common start hour


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station


    # display most commonly used end station


    # display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time


    # display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types


    # Display counts of gender


    # Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
