import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    filter_men = df[df["sex"] == "Male"]
    average_age_men = round(filter_men['age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    filter_bachelors = df[df["education"] == "Bachelors"]
    percentage_bachelors = round((filter_bachelors.shape[0]/df.shape[0])*100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    # dataframes with advanced education
    df_adv = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    df_adv_50k = df_adv[df_adv['salary'] == '>50K']
    # dataframes with lower education
    df_n = df[~df.index.isin(df_adv.index)]
    df_n_50k = df_n[df_n['salary'] == '>50K']

    # percentage with salary >50K
    higher_education_rich = round((df_adv_50k.shape[0]/df_adv.shape[0])*100, 1)
    lower_education_rich = round((df_n_50k.shape[0]/df_n.shape[0])*100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()
    df_min = df[df['hours-per-week'] == min_work_hours]
    df_min_50k = df_min[df_min['salary'] == '>50K']

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df_min.shape[0]

    rich_percentage = round((df_min_50k.shape[0]/df_min.shape[0])*100, 1)

    # What country has the highest percentage of people that earn >50K
    percentage = (df['salary'] == '>50K').groupby(df['native-country']).mean() * 100
    highest_earning_country = percentage.idxmax()
    highest_earning_country_percentage = round(percentage.max(), 1)

    # Identify the most popular occupation for those who earn >50K in India.
    df_in_50k = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    df_top_occupation = df_in_50k['occupation'].value_counts()
    top_IN_occupation = df_top_occupation.index[0]

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
