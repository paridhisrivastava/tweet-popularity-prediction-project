__author__ = 'Aditya Murthy'
__author__ = 'Paridhi Srivastava'
__author__ = 'Vatsala Singh'

# program to label the data based on the popularity of the tweets
import csv
import numpy

def main():
    #read the file and store the data into an array
    data = []
    retweets = {}
    favorites = {}
    with open('CleanedFeaturesOnly.csv', 'r', encoding="latin1") as f:
        reader = csv.reader(f)
        i = 0
        for row in reader:
            data.append(list(row))
            if i == 0:
                i+=1
                continue
            elif row[1] not in retweets.keys():
                retweets[row[1]] = []
                favorites[row[1]] = []
                retweets[row[1]].append(int(row[7]))
                favorites[row[1]].append(int(row[8]))
            else:
                retweets[row[1]].append(int(row[7]))
                favorites[row[1]].append(int(row[8]))
            i+=1

    #popularity labelling based on the retweets
    #calculate the active follower for each user
    avgRetDict = {}
    for key,value in retweets.items():
        avgRetDict[key] = sum(value)/ float(len(value))

    #calculate the popularity of each tweet
    newdata = numpy.array(data)
    newRetcol = [int(val[7])/avgRetDict[val[1]] for val in newdata[1:]]

    #threshold the popularity to label the data
    lowRange = 0.16
    highRange = 0.77
    pop = [0 if val<lowRange else 1 if val<highRange else 2 for val in newRetcol]

    popname_ret = ['retweet_popularity_label']
    pop_ret = numpy.concatenate((popname_ret,pop),axis=0)

    name = ['retweet_popularity_label']
    newRetcol = numpy.concatenate((name,newRetcol),axis=0)

    #popularity labelling based on the favorites
    #calculate the active follower for each user
    avgFavDict = {}
    for key,value in favorites.items():
        avgFavDict[key] = sum(value)/ float(len(value))

    #calculate the popularity of each tweet
    newdata = numpy.array(data)
    newFavcol = [int(val[8])/avgFavDict[val[1]] if avgFavDict[val[1]] > 0 else 0 for val in newdata[1:]]

    #threshold the popularity to label the data
    lowRange = 0.16
    highRange = 0.77
    pop = [0 if val<lowRange else 1 if val<highRange else 2 for val in newFavcol]


    #add the labelled columns to the original data and write to a csv file
    popname_fav = ['fav_popularity_label']
    pop_fav = numpy.concatenate((popname_fav,pop),axis=0)
    name = ['fav_popularity']
    newFavcol = numpy.concatenate((name,newFavcol),axis=0)

    all_data = numpy.column_stack((newdata, numpy.array([newRetcol]).T))
    all_data = numpy.column_stack((all_data, numpy.array([pop_ret]).T))

    all_data = numpy.column_stack((all_data, numpy.array([newFavcol]).T))
    all_data = numpy.column_stack((all_data, numpy.array([pop_fav]).T))

    with open("LabelledData.csv", 'wt', encoding="latin1", newline='') as f:
        csv.writer(f).writerows(all_data)



if __name__=="__main__":
    main()