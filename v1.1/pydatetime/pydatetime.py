from datetime import date
from datetime import time
from datetime import datetime
import datetime
import os
import time

def date_today(format):

    """Get the current date

    :param format: The first column on the output date
    :values: "dmy" or "mdy" or "ymd"
    :type format: str
    
    """
    today = date.today()
    if format == "dmy":
        today = date.today()
        return today.strftime("%d/%m/%Y")
    elif format == "mdy":
        today = date.today()
        return today.strftime("%m/%d/%Y")     
    elif format == "ymd":
        today = date.today()
        return today.strftime("%Y/%m/%d")
            

def time_now(format):
    """
    Get the current time

    :param format: the format in which it is displayed
    :type format: int
    :param format values: 24 or 12 for 24h or 12h clocks
    """
    nowtime = datetime.datetime.now()
    if format == 24:
        return nowtime.strftime("%H:%M:%S")
    elif format == 12:
        return nowtime.strftime("%I:%M:%S")

def weekday(length):
    """
    Get the current weekday

    :param length: If it is in short format like 'Wed', or full, like 'Wednesday'
    :type length: str
    :param length values: "short" or "full"
    """
    today = datetime.datetime.today()
    if length == "short":
        return today.strftime("%a")
    elif length == "full":
        return today.strftime("%A")

def current():
    """
    Gets the exact date and time
    """
    return datetime.datetime.now()

def day_weekday(day, month, year):
    """
    Gets the weekday of a specific date

    :param day: Takes the day of the month
    :type day: int

    :param month: Takes the month of the day
    :type month: int
    
    :param year: Takes the year of the day
    :type year: int
    """

    day = datetime.datetime(year, month, day)
    return day.strftime("%A")

def countdown(length):
    """
    Prints a second-by-second countdown of a specified length, using the current time

    :param length: In seconds, how long from start time it should last
    """

    for i in range(0, length):
        os.system('CLS')
        today = datetime.datetime.now()
        print(today.strftime("%I:%M:%S"))
        time.sleep(1)
    print("Done")

