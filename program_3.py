# Author: Faith Lamah
# Date: 10/17/2025
# Program #3: US_Population
def main():
    # Have the user input (using a loop) various information that contains three pieces of data: 
    # year, name of state, and population.  
    # Store all of this information in a list of lists.  For example it might be stored like this:
    
    # [[2010, "Maine", 1987435], [2010,"Minnesota",6873202], [2011, "Iowa", 3421988]]
    all_entered_values = []

    another_state = 'y'
    while another_state == 'y' or another_state == 'Y':
        year = int(input('Year: '))
        state = input('What state is it?')
        population = int(input('How many people are there?'))
        all_entered_values.append([year, state, population])
        another_state = input('Would you like to add another state? y = yes')

    year_to_use = int(input('What year would you like to sum the population for?'))

    sum_population_for_year(all_entered_values, year_to_use)
    # The program will add the populations from all states in the list of list for that year only.
    # Pass the list and year to the sum_population_for_year

def sum_population_for_year(all_entered_values, year_to_sum):
    # Loop through and sum the populations for the appropriate year.
    # e.g. for the list on line 7 the total would be 8,860,637 if the user enterd 2010 for the year to sum,
    # or 3,421,988 if they enterd 2011 for the year to sum.
    total_population = 0
    for entry in all_entered_values:
        if entry[0] == year_to_sum:
            total_population += entry[2]
    print(f'The total population for {year_to_sum} is {total_population} people.')

    # print the totalled population


# Call the main function.
if __name__ == '__main__':
    main()