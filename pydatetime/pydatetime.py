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

def ctime(format):
    """
    Get the current time in a customisable format, like only seconds or minute then seconds.

    :param format: The format in which it is returned, in abbreviations, like 'hms' for hour, minute, then second
    :type format: str
    """

    

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

def date_in_words(format):
    """
    Gets current date in word format, e.g. 31 Dec 2021

    :param format: specify what length, like Dec or December
    :type format: str
    :values format: "short" or "full"
    """
    today = datetime.datetime.now()
    if format == "short":
        return today.strftime("%d %b %Y")
    elif format == "full":
        return today.strftime("%d %B %Y")

def wait(length):
    """
    Pauses the program for a certain amount of time

    :param length: In seconds, how long the pause should be
    :type length: int
    """

    time.sleep(length)
    return

class clock:
    def full(length, clear):
        """
        Counts the time sequentially, clering the screen each time if specified

        :param length: In seconds, how long it should count for
        :param clear: In binary, 0 or 1, if it should clear the terminal inbetween counts or not
        """
        for i in range(0, length):
            if clear == 1:
                os.system('cls')
                print(time_now(24))
                time.sleep(1)
            elif clear == 0 :
                print(time_now(24))
                time.sleep(1)
    
    def seconds(length, clear):
        """
        Counts the time sequentially, clering the screen each time if specified, only using the current second

        :param length: In seconds, how long it should count for
        :param clear: In binary, 0 or 1, if it should clear the terminal inbetween counts or not
        """
        for i in range (0,length):
            if clear == 1:
                os.system('cls')
                print(time_now(24))
                time.sleep(1)
            elif clear == 0 :
                print(time_now(24))
                time.sleep(1)

