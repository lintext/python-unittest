import csv
def readzsmc():
    stream=open(r"D:\视频\\testdata.csv")
    data=csv.reader(stream)
    list=[]
    i=0
    for row in data:
        if i!=0:
            list.append(row)
        i=i+1
    return list
if __name__ == '__main__':
    data=readzsmc()
    for row in data:
        print(row)