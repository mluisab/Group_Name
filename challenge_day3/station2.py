
import datetime

# Defined function to call solution station 2
def solution_station_2(date_str):
    #loop to find the correlation between date and day of the week using datatime function
    try:

        date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d")
        
        # (0 = Monday, 6 = Sunday)
        day_of_week = date_obj.weekday()
        
        # Define a list of day names translated
        days_of_the_week_translated = ["月曜日", "火曜日", "水曜日", "木曜日", "金曜日", "土曜日", "日曜日"]
    
        
        # Return the corresponding day of the week
        return days_of_the_week_translated[day_of_week]
    except ValueError:
        return "Invalid date format. Please use YYYY-MM-DD."


