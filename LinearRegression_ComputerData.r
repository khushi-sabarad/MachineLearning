# Set working directory
setwd("C:/Users/Khushi/OneDrive/Desktop/data+codes/datasets")

# Load necessary libraries
library(dplyr)
library(caTools)

# Load data
Computer_data <- read.csv("Computer_data.csv", na.strings = "")

# Remove unnecessary columns
Computer_data <- Computer_data[-c(1, 8, 9, 10, 11)]

# Calculate correlations
cor_speed <- cor(Computer_data$price, Computer_data$speed)
cor_hd <- cor(Computer_data$price, Computer_data$hd)

# Perform ANOVA for RAM and CD
anov_ram <- aov(price ~ ram, data = Computer_data)
summary(anov_ram)
anov_cd <- aov(price ~ cd, data = Computer_data)
summary(anov_cd)

# Create boxplot
boxplot(Computer_data$price)

# Split data into training and testing sets
sample_indices <- sample.split(Computer_data$price, SplitRatio = 0.70)
trainingset <- Computer_data[sample_indices == TRUE, ]
testset <- Computer_data[sample_indices == FALSE, ]

# Build linear regression model
model <- lm(price ~ ., data = trainingset)

# Predict prices on the test set
testset$predicted_price <- predict(model, testset)

# Calculate correlation between actual and predicted prices
cor_predicted <- cor(testset$price, testset$predicted_price)

# Rename column using dplyr
a <- Computer_data %>% rename(screen_size = screen)

# Calculate mean and median for price and HD
mean_price <- mean(a$price)
median_price <- median(a$price)
mean_hd <- mean(a$hd)
median_hd <- median(a$hd)

# Select columns without "m" prefix
b <- select(a, -starts_with("m"))

