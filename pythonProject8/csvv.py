import csv
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import ddt


def getcsv():
    url = open('testdata.csv', 'r', encoding='utf-8')
    data = csv.reader(url)
    str = []
    next(data)
    i = 0
    for we in data:
        if we != 0:
            str.append(we)
            i = i + 1
    return str


if __name__ == '__main__':
    data = getcsv()
    for we in data:
        print(we)
