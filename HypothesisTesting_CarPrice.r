# Multivariate Statistics
# Hypothesis Testing

# One-sample t-test
# setwd("C:/path/...")
data <- read.csv("CarPrice_Assignment.csv")
View(data)

# Null Hypothesis (H0): Mean enginesize = 120
# Significance level (alpha) = 0.05
mean(data$enginesize) # Mean enginesize = 126.9073

# Two-sided test (Mean enginesize != 120)
result_two_sided <- t.test(data$enginesize, mu = 120, alternative = "two.sided", conf.level = 0.95)
print(result_two_sided) # p-value = 0.01848
# Interpretation: Since p-value (0.01848) < alpha (0.05), we reject the null hypothesis.
# Conclusion: There is statistically significant evidence that the mean enginesize is *different* from 120.

# One-sided (greater than) test (Mean enginesize > 120)
result_greater <- t.test(data$enginesize, mu = 120, alternative = "greater", conf.level = 0.95)
print(result_greater) # p-value = 0.00924
# Interpretation: Since p-value (0.00924) < alpha (0.05), we reject the null hypothesis.
# Conclusion: There is statistically significant evidence that the mean enginesize is *greater* than 120.

# One-sided (less than) test (Mean enginesize < 120)
result_less <- t.test(data$enginesize, mu = 120, alternative = "less", conf.level = 0.95)
print(result_less) # p-value = 0.9908
# Interpretation: Since p-value (0.9908) > alpha (0.05), we fail to reject the null hypothesis.
# Conclusion: There is *not* enough evidence to conclude that the mean enginesize is *less* than 120.
