# This script builds a classifier for first type of labelling
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
# construct the model 
model <- multinom(retweet_popularity_label.1 ~ tweet_id + followers_count + following_count + mentioned_count + from_user_favourites_count + tweets_count + retweet_count + favorite_count + urls_count + hashtags_count + mentions_count + day_of_the_week + time_of_the_day + number_of_tweet_chars + account_age, data = trainingData, na.action = na.exclude)
# find the most important features
mostImpVar <- varImp(model)
mostImpVar$Variables <- row.names(mostImpVar)
mostImpVar <- mostImpVar[order(-mostImpVar$Overall),]
print(head(mostImpVar))

coeffs = coefficients(model); print(exp(coeffs))
# predict the label of test data
predicted <- predict(model, testData)
#print(head(predicted))

# prints the accuracy
print(postResample(testData$retweet_popularity_label.1, predicted))
#print(confidence)


#write.csv(predictedValues, "Predicted.csv")
# plots the step wise correlated features
leaps<-regsubsets(retweet_popularity_label.1 ~ tweet_id + followers_count + following_count + mentioned_count + from_user_favourites_count + tweets_count + retweet_count + favorite_count + urls_count + hashtags_count + mentions_count + day_of_the_week + time_of_the_day + number_of_tweet_chars + account_age, data = trainingData,nbest=10)
plot(leaps,scale="r2")




