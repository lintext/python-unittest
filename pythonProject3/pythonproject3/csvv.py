import csv


def getcsv():
    url = open('testdata.csv', 'r', encoding="utf-8")
    data = csv.reader(url)
    str = []
    i = 0
    for we in data:
        if i != 0:
            str.append(we)
        i = i + 1
    return str


if __name__ == '__main__':
    data = getcsv()
    for we in data:
        print(we)
