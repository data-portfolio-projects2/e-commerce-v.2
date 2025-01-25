library(dplyr)

print_data_message <- function(message) {
  print(message)
}

calculate_descriptive_stats <- function(data) {
  summarise(data,
            Avg_Age       = mean(Age),
            Median_Age    = median(Age),
            Age_SD        = sd(Age),
            Avg_Income    = mean(Income_Level),
            Median_Income = median(Income_Level),
            Income_SD     = sd(Income_Level))
}

summarize_categorical_data <- function(data) {
  list(
    Location_Distribution = table(data$Location),
    Gender_Distribution   = table(data$Gender)
  )
}

EDA <- setRefClass("EDA",
                   fields = list(data = "data.frame"),
                   methods = list(
                     print_data = function() {
                       print_data_message("Simulated Demographics Data")
                       print(data)
                     },
                     
                     descriptive_stats = function() {
                       calculate_descriptive_stats(data)
                     },
                     
                     summary_categorical = function() {
                       summarize_categorical_data(data)
                     }
                   ))

run_eda_pipeline <- function(demographics) {
  eda <- EDA$new(data = demographics)
  
  eda$print_data()
