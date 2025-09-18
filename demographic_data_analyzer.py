import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')


    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_of_men_mask = df['sex'] == 'Male'
    average_age_men = df[average_age_of_men_mask]['age'].mean().round(1)

    # What is the percentage of people who have a Bachelor's degree?
    bachelors_mask = df['education'] == 'Bachelors'
    percentage_bachelors = (bachelors_mask.mean() * 100).round(1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    advanced_edu_mask = ((df['education'] == 'Bachelors')
                         | (df['education'] == 'Masters')
                         | (df['education'] == 'Doctorate'))
    lower_edu_mask = ((df['education'] != 'Bachelors')
                      & (df['education'] != 'Masters')
                      & (df['education'] != 'Doctorate'))
    salary_mask = df['salary'] == ">50K"

    # percentage with salary >50K
    higher_education_rich = ((salary_mask & advanced_edu_mask).sum() / advanced_edu_mask.sum() * 100).round(1)
    lower_education_rich = ((salary_mask & lower_edu_mask).sum() / lower_edu_mask.sum() * 100).round(1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_hours_mask = min_work_hours == df['hours-per-week']

    rich_percentage = (min_hours_mask & salary_mask).sum() / min_hours_mask.sum() * 100

    # What country has the highest percentage of people that earn >50K?
    countries_total = df['native-country'].value_counts()
    highest_earning_country = (df[salary_mask]['native-country'].value_counts() / countries_total * 100).sort_values(ascending=False).index[0]
    highest_earning_country_percentage = (df[salary_mask]['native-country'].value_counts() / countries_total * 100).sort_values(ascending=False).values[0].round(1)

    # Identify the most popular occupation for those who earn >50K in India.
    country_india_mask = df['native-country'] == 'India'
    top_IN_occupation = df[salary_mask & country_india_mask]['occupation'].value_counts().index[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
calculate_demographic_data()