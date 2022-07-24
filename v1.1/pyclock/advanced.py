from datetime import date
from datetime import time
from datetime import datetime
import datetime

def date_today(format, spacers):

    """Get the current date

    :param format: The first column on the output date
    :values: "ddmmyy" or "mmddyy" or "yymmdd"
    :type format: str

    :param spacers: The value used to space digits/letters
    :param spacers format: str
    :param spacers values: Can be any period, character or number
    : param spacers defaults: default value is "/"
    
    """
    if format == "ddmmyy":
        today = date.today()
        if spacers == "":
            return today.strftime("%d/%m/%Y")
        else:
            return today.strftime(f"%d{spacers}%m{spacers}%Y")
    elif format == "mmddyy":
        today = date.today()
        if spacers == "":
            return today.strftime("%m/%d/%Y")
        else:
            return today.strftime(f"%m{spacers}%d{spacers}%Y")
    elif format == "yymmdd":
        today = date.today()
        if spacers == "":
            return today.strftime("%Y/%m/%d")
        else:
            return today.strftime(f"%Y{spacers}%m{spacers}%d")

def time_now(format):
    """
    Get the current time

    :param format: the fornat in which it is displayed
    :param format type: int
    :param format values: 24 or 12 for 24h or 12h clocks
    """
    nowtime = datetime.datetime.now()
    if format == 24:
        return nowtime.strftime("%H:%M:%S")
    elif format == 12:
        return nowtime.strftime("%I:%M:%S")