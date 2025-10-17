# Author: Faith Lamah
# Date: 10/17/2025
# Program #1: Rainfall
# Design a program that lets the user enter the total rainfall for each of 12 months into a list.
# The program should calculate and display the total rainfall for the year, 
# the average monthly rainfall, # and the months with the highest and lowest amounts.

def total_rainfall():
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    monthly_rainfall = []
    total_rainfall = 0
    for rain in range(12):
        months_rain = int(input(f'How much rain was in {months[rain]}?'))
        monthly_rainfall.append(months_rain)
        total_rainfall += months_rain
    max_rainfall = monthly_rainfall.index(max(monthly_rainfall))
    min_rainfall = monthly_rainfall.index(min(monthly_rainfall))
    print(f'The total rainfall for the year is {total_rainfall} inches.')
    print(f'The average monthly rainfall is {total_rainfall/len(monthly_rainfall)} inches.')
    print(f'The month with the highest rainfall is {months[max_rainfall]}.')
    print(f'The month with the lowest rainfall is {months[min_rainfall]}.')
total_rainfall()
