#which day of the week it is on the day 
#and then translate that day
import datetime

# Get user input for a date in the format YYYY-MM-DD
date_str = input("Enter a date from the years 2023-34 in this format (YYYY-MM-DD): ")
#loop to asses which day of the week the date is using the datetime function
try:
   
    date_object = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    
    # Get the day of the week (0 = Monday to 6 = Sunday)
    day_of_week = date_object.weekday()
    
    # Define a list of day names in Chinese 
    days_of_the_week_translated = ["月曜日", "火曜日", "水曜日", "木曜日", "金曜日", "土曜日", "日曜日"]
    
    # Print the corresponding day of the week
    print(f"The day of the week for {date_str} is {days_of_the_week_translated[day_of_week]}.")
#if the format is wrong ask for it to be inputed again
except ValueError:
    print("Invalid date format. Please use YYYY-MM-DD.")
