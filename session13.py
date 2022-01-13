import csv
from collections import namedtuple
from datetime import datetime


def get_row():
    """
    To get the data in a namedtuple, I have opened the csv file and stored the reader as 'csv_reader'.
    I read the first row which is the name of Columns and turned them into variable names and stored them in a list.
    For Eg, Plate ID becomes Plate_ID, Violation Code becomes Violation_Code.
    This list called 'temp' is going to be the list of fieldnames of our namedtuple.
    I iterated through the file and yielded a namedtuple with data in row as parameters of appropriate Datatypes.
    I used yield so get_row() is a generator.
    """
    with open("nyc_parking_tickets_extract-1.csv", 'r') as f:
        csv_reader = csv.reader(f)
        temp = ["_".join(i.split(" ")) for i in next(csv_reader)]
        dta = namedtuple('dta', temp)
        for row in csv_reader:
            yield dta(int(row[0]), row[1], row[2], row[3], datetime.strptime(row[4], "%m/%d/%Y"), int(row[5]), row[6],
                      row[7], row[8])


dct = {}


def get_violations(car: str):
    """
    This is a function will return number of violations of a Particular car given as a parameter.
    The values are stored in a global dictionary.
    If the dictionary already has the value we are looking for, it will just return that.
    But when the dictionary is empty i.e. the get_violations() has never been called before it will perform some task.
    It will iterate through the generator and count the values and store it in the dictionary.
    """
    if car in dct.keys():
        return dct[car]
    a = get_row()
    for i in a:
        car_type = i.Vehicle_Make
        if car_type in dct.keys():
            dct[car_type] += 1
        else:
            dct[car_type] = int(1)
    return dct[car]


