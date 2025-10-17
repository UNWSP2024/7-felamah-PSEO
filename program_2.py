# Author: Faith Lamah
# Date: 10/17/2025
# Program #2: Larger than n
# In a program, write a function (with NO output) that accepts two arguments: number n, and a list.
# Assume that the list contains numbers.
# The function shell has been written out on line 30, (def display_larger_than_n_list)
# and should display all of the numbers in the list that are greater than then number n.

def main():
    # Declare local variables
    compare_number = int(input('What should the numbers be greater than?'))
    number_list = []

    another_number = 'y'
    while another_number == 'y':
        number = int(input('Number that should be added to list: '))
        print('Number:', number)
        number_list.append(number)
        another_number = input('Should another number be added to list? y = yes')

    print('List of numbers:')
    print(number_list)

    print(f'List of numbers that are larger than {compare_number}:')

    display_larger_than_n_list(compare_number, number_list)

def display_larger_than_n_list(n, n_list):
    # Write your code to display all of the numbers in the list that are greater than then number n. below
    numbersLargerthanNumber = []
    print('In display_larger_than_n_list')
    for number in n_list:
        if number > n:
            numbersLargerthanNumber.append(number)
    print(numbersLargerthanNumber)



# Call the main function.
if __name__ == '__main__':
    main()