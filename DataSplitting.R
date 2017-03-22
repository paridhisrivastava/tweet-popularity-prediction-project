# This script splits the data into training and testing
# Authors
# Aditya Murthy
# Paridi Srivastava
# Vatsala Singh
library(caret)
# read the data from csv file
data <- read.csv("Popularity_LabelledData.csv")
# setting the seed
splitSize <- floor(0.70*nrow(data))
set.seed(42)
# find the training index
trainIndx <- sample(seq_len(nrow(data)), size = splitSize)
# split the training data
trainingData <- data[trainIndx, ]
# split the test data
test <- data[-trainIndx, ]
# write the data back to a csv file
write.csv(trainingData, file = "TrainingData.csv")
write.csv(test, file = "TestData.csv")

