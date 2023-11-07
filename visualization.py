import time
import pandas as pd
import matplotlib.pyplot as plt


def read_csv_file():
    """
    Read a CSV file containing world population data.
    
    Returns:
        pd.DataFrame: DataFrame containing the world population data.
    """
    data = pd.read_csv('E:/jupyter notebook/asad/world_population.csv')
    return data


def renaming_columns(dataframe):
    """
    Modify DataFrame columns and clean data.

    Args:
        df (pd.DataFrame): Input DataFrame.

    Returns:
        pd.DataFrame: Modified DataFrame.
    """

    # selecting data for the last 10 years
    dataframe.columns = dataframe.columns.str.lower()

    # renaming columns for better understanding
    dataframe.rename(columns={'country/territory': 'country', '2022 population': 'pop_2022', '2020 population': 'pop_2020', '2015 population': 'pop_2015', '2010 population': 'pop_2010', '2000 population': 'pop_2000', '1990 population': 'pop_1990',
                     '1980 population': 'pop_1980', '1970 population': 'pop_1970', 'area (km²)': 'area_sqkm', 'density (per km²)': 'density_per_sqkm', 'growth rate': 'growth_rate', 'world population percentage': 'world_pop_%age'}, inplace=True)
    dataframe = dataframe[['rank', 'country', 'continent', 'pop_2022', 'pop_2020', 'pop_2015',
                           'pop_2010', 'pop_2000', 'pop_1990', 'pop_1980', 'pop_1970', 'growth_rate', 'world_pop_%age']]
    return dataframe


def lineplot(data):
    """
    Generate a line plot to visualize population trends for the top 5 ranked countries.

    Args:
        data (pd.DataFrame): DataFrame containing population data for various years.

    Returns:
        None
    """
    # Filtering data for top 5 ranked countries and sort by rank
    data = data[data['rank'] <= 5]
    data.sort_values(by=['rank'], inplace=True)

    years = ['1970', '1980', '1990', '2000', '2010', '2015',
             '2020', '2022']  # Years to be plotted (in reverse order)

    # line colors for each country
    line_colors = ['black', 'blue', 'red', 'cyan', 'yellow', 'yellow']

    # Creating the line plots for each country
    plt.figure(figsize=(10, 6))
    for i, country in enumerate(data['country']):
        populations = [data.loc[data['country'] == country,
                                f'pop_{year}'].values[0] for year in years]
        plt.plot(years, populations, marker='o',
                 label=country, color=line_colors[i])

    plt.xlabel('Year')
    plt.ylabel('Population (in billions)')
    plt.title('Population Trends for Top 5 Ranked Countries')
    plt.legend()
    plt.show()


def piechart(data):
    """
    Generate a pie chart to visualize the percentage of world population by continent.

    Args:
        data (pd.DataFrame): DataFrame containing 'continent' and 'world_pop_%age' columns.

    Returns:
        None
    """
    # Grouping data by continent and sum the world_pop_%age for each continent
    continent_pop = data.groupby('continent')['world_pop_%age'].sum()

    # Creating a pie chart
    plt.figure(figsize=(8, 8))
    plt.pie(continent_pop, labels=continent_pop.index, autopct='%1.1f%%', startangle=140,
            colors=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6'])
    plt.title('World Population Percentage by Continent')
    plt.axis('equal')
    plt.show()


def barchart(data):
    """
    Create a horizontal bar chart to display the total population by continent in 2022.

    Parameters:
        data (DataFrame): Input DataFrame with 'continent' and 'pop_2022' columns.

    Returns:
        None (displays the plot).

    """
    # Grouping data by continent and calculate the total population for 2022
    continent_population_2022 = data.groupby('continent')['pop_2022'].sum()

    # Sorting continents by total population in ascending order
    continent_population_2022 = continent_population_2022.sort_values(
        ascending=True)

    # Creating a horizontal bar chart with yellow bars
    plt.figure(figsize=(15, 6))
    bars = plt.barh(continent_population_2022.index,
                    continent_population_2022.values, color='yellow')
    plt.xlabel('Total Population in 2022 (in billions)')
    plt.ylabel('Continent')
    plt.title('Total Population by Continent in 2022')

    # Adding population numbers on top of the bars
    for bar in bars:
        plt.text(bar.get_width() - 0.1*bar.get_width(), bar.get_y() + bar.get_height()/2, f'{int(bar.get_width()):,}',
                 va='center', ha='left', color='blue', fontsize=10)

    plt.show()


if __name__ == '__main__':
    start_time = time.time()
    print(f'Started at {time.ctime(start_time)}')

    # Read the csv file
    data = read_csv_file()

    # Rename columns
    data = renaming_columns(dataframe=data)

    # Line plot
    lineplot(data)

    # Pie chart
    piechart(data)

    # Bar chart
    barchart(data)

    end_time = time.time()
    print(f'Ended at {time.ctime(end_time)}')

    execution_time = end_time - start_time
    print(f'Execution time: {execution_time:.2f} seconds')
