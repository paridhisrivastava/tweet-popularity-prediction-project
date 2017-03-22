__author__ = 'Aditya Murthy'
__author__ = 'Paridhi Srivastava'
__author__ = 'Vatsala Singh'

import csv
import numpy
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn import metrics
import pandas
from pandas_confusion import ConfusionMatrix
import matplotlib.pyplot as plt


#build a RandomForest Classification model to predict the popularity of a tweet
#using Retweet based labelling as the target class
def main():
    #read the training data and store in an array
    train_data = []
    with open('TrainingData.csv', 'r', encoding="latin1") as f:
        reader = csv.reader(f)
        for row in reader:
            train_data.append(list(row))
    traindata = numpy.array(train_data)

    #read the training data and store in an array
    test_data = []
    with open('TestData.csv', 'r', encoding="latin1") as f:
        reader = csv.reader(f)
        for row in reader:
            test_data.append(list(row))
    testdata = numpy.array(test_data)

    #build a RandomForestClassifier model using the training data and the target class
    #target class is the favorite based popularity labelled column
    train_target = numpy.ravel(traindata[1:, [20]])
    traindata = numpy.delete(traindata[1:], [17, 18, 19, 20], axis=1)
    traindata = (numpy.delete(traindata, [0, 1, 2], axis=1))
    traindata = numpy.array(traindata)
    rf = RandomForestClassifier(n_estimators=100)
    rf.fit(traindata, train_target)

    #get the features and their relative importance in the prediction of the tweet
    #popularity and plot them
    names = traindata[0:1][0]
    names = names[:17]
    names = names[3:]
    feature_vals = (rf.feature_importances_)
    features = dict(zip(names, feature_vals))
    plt.bar(range(len(features)), features.values(), align='center')
    locations, labels = plt.xticks(range(len(features)), list(features.keys()))
    plt.setp(labels, rotation=90, fontsize=5)
    plt.suptitle('Significance of Features in Prediction of Popularity by Favorite Count', fontsize=14)
    plt.xlabel('Features', fontsize=12)
    plt.ylabel('Feature values', fontsize=12)
    plt.savefig('favs_feature_importance.png')

    #apply the RandomForest classification model on the test data to predict the popularity class label
    test_target = numpy.ravel(testdata[1:, [20]])
    testdata = numpy.delete(testdata[1:], [17, 18, 19, 20], axis=1)
    testdata = numpy.array(numpy.delete(testdata, [0, 1, 2], axis=1))
    pre = rf.predict(testdata)

    #get the Confusion Matrix and the accuracy for the predicted data
    actClass = pandas.Series(test_target, name='Dataset class')
    predClass = pandas.Series(pre, name='Predicted Class')
    confusionMat = ConfusionMatrix(actClass, predClass)
    print('Confusion Matrix of Random Forest')
    print(confusionMat)
    acc = metrics.accuracy_score(test_target, pre)
    print('Accuracy of Random Forest:', acc)


if __name__=="__main__":
    main()
