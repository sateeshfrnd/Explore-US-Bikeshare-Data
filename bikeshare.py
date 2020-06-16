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

def display_raw_data(df):
    """Display the raw data upon request by user that to compute the Statistics"""
    rasw_df = df.drop(['month', 'day_of_week', 'hour'], axis=1)
    index = 0
    display_record_count = 5

    view_data = input('\nWould you like to view the data that to compute the stats? Enter yes or no.\n')
    while True:
        if view_data.lower() == 'no':
            return
        if view_data.lower() == 'yes':
            print(df[index: index + display_record_count])
            index = index + display_record_count

        view_data = input('\nWould you like to view 5 more records of the data that to compute the stats? Enter yes or no.\n')

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
    most_common_month = df['month'].mode()[0]
    print('The most common month is {}'.format(MONTHS[most_common_month].title()))

    # display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print('The most common day of week is {}'.format(most_common_day))

    # display the most common start hour
    most_common_hour = df['hour'].mode()[0]
    print('The most common start hour is {}'.format(most_common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_used_start_station = df[['Start Station']].groupby(['Start Station']).size().nlargest(1)
    print('Most commonly used start station is "{}"'.format(most_used_start_station.index[0]))

    # display most commonly used end station
    most_used_end_station = df[['End Station']].groupby(['End Station']).size().nlargest(1)
    print('Most commonly used end station is "{}"'.format(most_used_end_station.index[0]))

    # display most frequent combination of start station and end station trip
    most_used_start_end_station = df[['Start Station', 'End Station']].groupby(
        ['Start Station', 'End Station']).size().nlargest(1)
    print('The most frequent combination of start station and end station trip is "{}" and "{}"'.format(
        most_used_start_end_station.index[0][0], most_used_start_end_station.index[0][1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    df['Trip Duration'] = pd.to_datetime(df['End Time']) - df['Start Time']

    # display total travel time
    trip_total_duration = df['Trip Duration'].sum()
    print('Total trip duration is "{}"'.format(trip_total_duration))

    # display mean travel time
    trip_average_duration = df['Trip Duration'].mean()
    print('Average trip duration is "{}"'.format(trip_average_duration))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type_counts = df.groupby('User Type')['User Type'].count()
    print('User Type count are :')
    print('-' * len('User Type count are :'))
    print(user_type_counts.to_string())

    # Display counts of gender
    print()
    try:
        gender_counts = df.groupby('Gender')['Gender'].count()
        print('Gender Count are :')
        print('-' * len('Gender Count are :'))
        print(gender_counts.to_string())
    except:
        print('There is no "Gender" column in data.')

    # Display earliest, most recent, and most common year of birth
    print()
    try:
        earliest_year = df['Birth Year'].min()
        print('\nEarliest year of birth : {}'.format(earliest_year))

        most_recent_year = df['Birth Year'].max()
        print('Most recent year of birth : {}'.format(most_recent_year))

        most_common_year = df['Birth Year'].mode()[0]
        print('Most common year of birth : {}'.format(most_common_year))
    except:
        print('There is no "Birth Year" column in data.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        display_raw_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
