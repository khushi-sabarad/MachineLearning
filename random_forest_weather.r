# Random Forest

## Setting Working Directory and Reading Data
setwd("../path")
wt=read.csv("weatherAUS.csv")
View(wt)
# Optional: Remove specific columns (uncomment if needed)
# wt <- wt[-c(1,2,6,7,18,19,23)]



## Data Preprocessing
# Checking & Handling missing values
sum(is.na(wt$Date))        
sum(is.na(wt$Location))    
sum(is.na(wt$RISK_MM))     
sum(is.na(wt$RainTomorrow))

# Replace missing values with median for numeric columns that is skewed or contains outliers, as the median is less sensitive to extreme values than the mean
numeric_columns <- c("MinTemp", "MaxTemp", "Rainfall", "Evaporation", "WindGustSpeed", 
                     "WindSpeed9am", "WindSpeed3pm", "Pressure9am", "Pressure3pm", 
                     "Temp9am", "Temp3pm", "Humidity9am")

for (col in numeric_columns) {
  wt[[col]][is.na(wt[[col]])] <- median(wt[[col]], na.rm = TRUE)
}

# Replace missing values with mean for numeric columns where mean is more appropriate (distribution is approximately normal)
mean_columns <- c("Humidity3pm", "Sunshine")

for (col in mean_columns) {
  wt[[col]][is.na(wt[[col]])] <- mean(wt[[col]], na.rm = TRUE)
}

# Replace missing categorical values with the mode (the most frequent value) ensures that the most common category is used.
table(wt$WindGustDir) #to find mode
wt$WindGustDir[is.na(wt$WindGustDir)]="W"

table(wt$WindDir9am) 
wt$WindDir9am[is.na(wt$WindDir9am)]="N"

table(wt$WindDir3pm) 
wt$WindDir3pm[is.na(wt$WindDir3pm)]="SE"

table(wt$Cloud9am)
wt$Cloud9am[is.na(wt$Cloud9am)]=7

table(wt$Cloud3pm)
wt$Cloud3pm[is.na(wt$Cloud3pm)]=7

table(wt$RainToday)
wt$RainToday[is.na(wt$RainToday)]="No"

# check if missing values still exist
total_missing <- sum(is.na(wt))
total_missing

## Installing and Loading Packages
# Install necessary packages if not already installed
if (!require("caTools")) install.packages("caTools")
if (!require("randomForest")) install.packages("randomForest")

# Load libraries
library(caTools)
library(randomForest)

## Model Training and Evaluation
## Splitting the Data
# Convert the output variable(RainTomorrow) to a factor
wt$RainTomorrow <- as.factor(wt$RainTomorrow)

# Split the data into training and testing sets
sample <- sample.split(wt$RainTomorrow, SplitRatio = 0.70)
train <- subset(wt, sample == TRUE)
test <- subset(wt, sample == FALSE)


# Training the Random Forest Model
model <- randomForest(RainTomorrow ~ ., data = train)

# Predict on the test set
test$Predicted <- predict(model, test)

# Confusion matrix
conf_matrix <- table(test$RainTomorrow, test$Predicted)
conf_matrix

# Calculating Accuracy
# Calculate accuracy manually
TN <- conf_matrix[1, 1]
TP <- conf_matrix[2, 2]
FN <- conf_matrix[1, 2]
FP <- conf_matrix[2, 1]

accuracy <- (TP + TN) / (TP + TN + FP + FN)
print(accuracy)

#        No    Yes
# No    (TN)   (FN)
# Yes   (FP)   (TP)