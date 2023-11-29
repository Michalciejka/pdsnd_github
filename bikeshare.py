import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


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
    # def read_user_data():
    while True:
        city1 = input("give me city: ")
        city = city1.lower()
        if city.lower() in ['chicago', 'new_york_city', 'washington']:
            break
        else:
            print("City is invalid, Please, change.")
    # print("City:", city)
    #    chicago = pd.read_csv(CITY_DATA['chicago'])
    #    new_york_city= pd.read_csv(CITY_DATA['new york city'])
    #    washington = pd.read_csv(CITY_DATA['washington'])
    #    return city
    # city = read_user_data()
    #

    

    #    month = input("give me month: ")
    while True:
        month1 = input("give me month: ")
        month = month1.lower()
        if month in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
            break
        else:
            print("Month is invalid, Please, change.")
    #    df1['Start Time'] = pd.to_datetime(df1['Start Time'])
    #    df1['month'] = df1['Start Time'].dt.month
    #    df2['Start Time'] = pd.to_datetime(df2['Start Time'])
    #    df2['month'] = df2['Start Time'].dt.month
    #    df3['Start Time'] = pd.to_datetime(df3['Start Time'])
    #    df3['month'] = df3['Start Time'].dt.month

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    #    day = input("give me day: ")
    while True:
        day1 = input("give me day: ")
        day = day1.lower()
        if day in ['monday', 'thuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
            break
        else:
            print("Day is invalid, Please, change.")
        #    day = df1['Start Time'].dt.weekday_name
    #    df1['Start Time'] = pd.to_datetime(df1['Start Time'])
    #    day = df1['Start Time'].dt.weekday_name
    #    df2['Start Time'] = pd.to_datetime(df2['Start Time'])
    #    day = df2['Start Time'].dt.weekday_name
    #    df3['Start Time'] = pd.to_datetime(df3['Start Time'])
    #    day= df3['Start Time'].dt.weekday_name
    #    print(day)
    print('-' * 40)
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
    # df = pd.read_csv(CITY_DATA['chicago'])
    file_path = f"{city}.csv"
    df = pd.read_csv(file_path)
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    month_mapping = {
        'january': 1,
        'february': 2,
        'march': 3,
        'april': 4,
        'may': 5,
        'june': 6,
        'all': None,
    }
    # df = df[(df['Start Time'].dt.month == month) & (df['Start Time'].dt.dayofweek == day)]
    if month in month_mapping:
        month_number = month_mapping[month]
        df = df[df['Start Time'].dt.month == month_number]
    # df = df[df['Start Time'].dt.month == month]
    # df = df[df['Start Time'].dt.dayofweek == day]
    day_mapping = {
        'monday': 1,
        'thuesday': 2,
        'wednesday': 3,
        'thursday': 4,
        'friday': 5,
        'saturday': 6,
        'sunday': 7,
        'all': None,
    }
    # df = df[(df['Start Time'].dt.month == month) & (df['Start Time'].dt.dayofweek == day)]
    if day in day_mapping:
        day_number = day_mapping[day]
        df = df[df['Start Time'].dt.dayofweek == day_number]
    df = df.sort_values(['Start Time'])
    i = 0
    print(df.iloc[0:5])
    while i < 5:
        print(df.iloc[i])
        i += 1
    question = input("Do you want to see the next 5 rows of data? yes/no)")
    while question.lower() == "yes":
        for j in range(i, i + 5):
            if j < len(df):
                print(df.iloc[j])
            else:
                break
        i += 5
        question = input("Do you want to see the next 5 rows of data? yes/no)")
        if question.lower() != "yes":
            break
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    print('Most Popular month:', popular_month)

    # TO DO: display the most common day of week
    df['days_of_week'] = df['Start Time'].dt.weekday_name
    popular_days_of_week = df['days_of_week'].mode()[0]
    print('Most Popular days_of_week:', popular_days_of_week)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    popular_start_station = df['Start Station'].value_counts()
    print(popular_start_station[0])

    # TO DO: display most commonly used end station

    popular_end_station = df['End Station'].value_counts()
    print(popular_end_station[0])

    # TO DO: display most frequent combination of start station and end station trip
    # 'Connected' = 'Start Station' + ' | ' + 'End Station'
    # popular_connected = df['Connected'].value_counts()
    # print(ppopular_connected[0])
    popular_stations = df.groupby(['Start Station', 'End Station']).size().reset_index(name='Count')

    popular_stations = popular_stations.sort_values(by='Count', ascending=False)

    most_popular = popular_stations.iloc[0]
    print("most frequent combination of start station and end station trip:")
    print("Start_Station:", most_popular['Start Station'])
    print("End Station:", most_popular['End Station'])
    print("Count:", most_popular['Count'])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print(df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print(df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()

    # TO DO: Display counts of gender
    user_types = df['User Type'].value_counts()

    # TO DO: Display earliest, most recent, and most common year of birth
    print(df['Birth Year'].min())
    print(df['Birth Year'].max())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


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
