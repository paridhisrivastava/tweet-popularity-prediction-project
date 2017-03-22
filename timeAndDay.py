__author__ = 'Aditya Murthy'
__author__ = 'Paridhi Srivastava'
__author__ = 'Vatsala Singh'
# Script to select only english tweets and extract time information
# by Aditya S Murthy, Paridhi Srivastava and  Vatsala Singh, 

import sys
import csv

def openFile(fn):
    """
    Function to  open the file and load the data from csv file
    :param fn: The filename and path of the csv file
    :return: The loaded data in a list of lists
    """

    with open(fn,'rU',encoding="utf8") as file: # open file
        reader=csv.reader(file)
        Data=list(list(line) for line in csv.reader(file,delimiter=','))

    return Data # return the data

def main():
    """
    Main function
    """
    fn=sys.argv[1] #file name as commandline arguments
    data=openFile(fn)
    print(len(data))

    firstRow=data[0] # extract data
    firstRow.append('day_of_the_week')
    firstRow.append('time_of_the_day')
    firstRow.append('number_of_tweet_chars')
    firstRow.append('account_age')
    days=['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
    print(firstRow)

    newdata=[]
    newdata.append(firstRow)

    data=data[1:]

    for row in data: # select only required data and calculate the required fetures
        if row[2]=='en':
            #print(row)
            time=row[3]
            time=time.split()
            yeardata=row[10].split()
            row.append(days.index(time[0])+1)
            row.append(time[3][0:2])
            row.append(len(row[4]))
            row.append(2016-int(yeardata[-1]))
            newdata.append(row)


    #print(newdata)

    with open('CleanedFeaturesOnly.csv','w',encoding="utf8",newline='') as file: # open file and write onto it
        writer=csv.writer(file)
        writer.writerows(newdata)


if __name__=='__main__':
    main()