from datetime import date
from datetime import time
from datetime import datetime
import datetime

def date_today(format, year):

    """Get the current date

    :param format: The first column on the output date
    :values: "dmy" or "mdy" or "ymd"
    :type format: str

    :param year: The length of the year column 
    :param year format: int
    :param year values: 2 or 4 digits
    
    """
    today = date.today()
    if format == "dmy":
        today = date.today()
        if year == 2:
            return today.strftime("%d/%m/%y")
        elif year == 4:
            return today.strftime("%d/%m/%Y")
    elif format == "mdy":
        today = date.today()
        if year == 2:
            return today.strftime("%m/%d/%y")
        elif year == 4:
            return today.strftime("%m/%d/%Y")
    elif format == "ymd":
        today = date.today()
        if year == 2:
            return today.strftime("%y/%m/%d")
        elif year == 4:
            return today.strftime("%Y/%m/%d")

def time_now(format):
    """
    Get the current time

    :param format: the format in which it is displayed
    :param format type: int
    :param format values: 24 or 12 for 24h or 12h clocks
    """
    nowtime = datetime.datetime.now()
    if format == 24:
        return nowtime.strftime("%H:%M:%S")
    elif format == 12:
        return nowtime.strftime("%I:%M:%S")

def date_words(length, format):
    """
    Get the current date in words like 31 Dec 2022
    """