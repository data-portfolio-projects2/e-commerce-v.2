library(dplyr)

set.seed(123)

demographics <- data.frame(
  Age          = sample(18:65, 10, replace = TRUE),
  Location     = sample(c("Urban", "Suburban", "Rural"), 10, replace = TRUE),
  Gender       = sample(c("Male", "Female"), 10, replace = TRUE),
  Income_Level = sample(20000:100000, 10, replace = TRUE)
)

EDA <- setRefClass("EDA",
                   fields = list(data = "data.frame"),
                   methods = list(
                     print_data = function() {
                       print("Simulated Demographics Data")
                       print(data)
                     },
                     
                     descriptive_stats = function() {
                       summarise(data,
                                 Avg_Age       = mean(Age),
                                 Median_Age    = median(Age),
                                 Age_SD        = sd(Age),
                                 Avg_Income    = mean(Income_Level),
                                 Median_Income = median(Income_Level),
                                 Income_SD     = sd(Income_Level))
                     },
                     
                     summary_categorical = function() {
                       list(
                         Location_Distribution = table(data$Location),
                         Gender_Distribution   = table(data$Gender)
                       )
                     }
                   ))

eda <- EDA$new(data = demographics)

eda$print_data()
descriptive_stats <- eda$descriptive_stats()
print("Descriptive Statistics")
print(descriptive_stats)

categorical_summary <- eda$summary_categorical()
print("Location Distribution")
print(categorical_summary$Location_Distribution)

print("Gender Distribution")
print(categorical_summary$Gender_Distribution)
