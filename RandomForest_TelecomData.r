#random forest
setwd("C:/Users/Khushi/OneDrive/Desktop/data+codes/datasets")
tele = read.csv("Telecom_Data.csv")
tele = tele [-c(4)]
tele$churn = as.factor(tele$churn)
library(caTools)
sample = sample.split(tele$churn,SplitRatio = 0.70)
train = subset (tele,sample == TRUE)
test = subset (tele,sample == FALSE)
library(randomForest)
model = randomForest(churn~.,data = train)
test$Predicted = predict(model,test)
table(test$churn,test$Predicted)
varImpPlot(model)

#   0   1
#0 TN   FN    
#1 FP   TP    

#accuracy =(TP+TN)/(TP+TN+FP+FN)
