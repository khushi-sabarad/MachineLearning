# Hypothesis Testing using R

Hypothesis testing is a statistical method used to make decisions about population parameters based on sample data.  It's a way to formally test a claim or hypothesis about a population.


The general process of hypothesis testing involves:

1. **Formulating Hypotheses:**
    * **Null Hypothesis (H0):** A statement about the population parameter that you are trying to disprove or reject. It often represents a statement of no effect.  It's the hypothesis you're testing *against*.
    * **Alternative Hypothesis (H1):** A statement that contradicts the null hypothesis. It's what you are trying to support with your data.  It's often what you believe to be true.

2. **Choosing a Significance Level (α):** This is the probability of rejecting the null hypothesis when it is actually true (Type I error, also called a "false positive").  Common values for alpha are 0.05 (5%) or 0.01 (1%).  It represents the level of risk you're willing to accept in making a Type I error. {α = 1-confidence level}

3. **Selecting a Test Statistic:** A value calculated from your sample data that is used to test the hypothesis. The choice of test statistic depends on the type of data (e.g., continuous, categorical) and the hypotheses being tested (e.g., testing a mean, testing a proportion, comparing two means).

4. **Calculating the P-value:** The probability of observing a test statistic as extreme as, or more extreme than, the one calculated from your sample data, *assuming the null hypothesis is true*.  The p-value is a measure of how likely it is to observe your data if the null hypothesis were actually true.

5. **Making a Decision:**
    * If p-value < α, you reject the null hypothesis.  This means there is sufficient evidence to support the alternative hypothesis.  The result is considered statistically significant.
    * If p-value >= α, you fail to reject the null hypothesis.  This does *not* mean the null hypothesis is true; it simply means there is not enough evidence to reject it.

**Important Considerations:**

* **One-tailed vs. Two-tailed Tests:** A one-tailed test is directional (e.g., testing if a mean is *greater than* a value, or if a mean is *less than* a value). A two-tailed test is non-directional (e.g., testing if a mean is *different from* a value).
* **Assumptions:** Many hypothesis tests have underlying assumptions about the data (e.g., normality, independence, equal variances). It's crucial to check these assumptions before performing a test.
* **Type I and Type II Errors:** There are two types of errors in hypothesis testing:
    * **Type I Error (False Positive):** Rejecting a true null hypothesis.
    * **Type II Error (False Negative):** Failing to reject a false null hypothesis.

## Code Example
[CarPriceAssignment](https://github.com/khushi-sabarad/MachineLearning/blob/main/HypothesisTesting_CarPrice.r)
