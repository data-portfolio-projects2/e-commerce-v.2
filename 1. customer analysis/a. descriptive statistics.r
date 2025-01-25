library(dplyr)

set.seed(123)  
demographics <- data.frame(
  Age = sample(18:65, 10, replace = TRUE),
  Location = sample(c("Urban", "Suburban", "Rural"), 10, replace = TRUE),
  Gender = sample(c("Male", "Female"), 10, replace = TRUE),
  Income_Level = sample(20000:100000, 10, replace = TRUE)
)

print("Simulated Demographics Data")
print(demographics)

descriptive_stats <- demographics %>%
  summarise(
    Avg_Age = mean(Age),
    Median_Age = median(Age),
    Age_SD = sd(Age),
    Avg_Income = mean(Income_Level),
    Median_Income = median(Income_Level),
    Income_SD = sd(Income_Level)
  )

print("Descriptive Statistics")
print(descriptive_stats)

# Summary of Categorical Variables
location_summary <- table(demographics$Location)
gender_summary <- table(demographics$Gender)

print("Location Distribution")
print(location_summary)

print("Gender Distribution")
print(gender_summary)
