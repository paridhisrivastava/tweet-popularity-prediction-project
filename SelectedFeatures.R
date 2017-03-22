# This script runs the classifier for the selected features for second type of labelling
# Authors
# Aditya Murthy
# Paridi Srivastava
# Vatsala Singh
library(leaps)
require(nnet)
library(caret)
# read the training and testing data from csv files

trainingData <- read.csv("TrainingData.csv")
testData <- read.csv("TestData.csv")
# model with selected features
model <- multinom(fav_popularity_label ~ tweet_id + retweet_count + favorite_count + urls_count + hashtags_count + mentions_count + day_of_the_week + number_of_tweet_chars, data = trainingData, na.action = na.exclude)
coeffs = coefficients(model); print(exp(coeffs))
# predict the labels using test data
predicted <- predict(model, testData)
# print the accuracy
print(postResample(testData$retweet_popularity_label.1, predicted))
write.csv(predicted, "PredictedWithFeatures.csv")





