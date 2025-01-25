set_seed_and_generate_campaign_data <- function() {
  set.seed(123)
  campaign_data <- data.frame(
    Group = sample(c("A", "B"), 1000, replace = TRUE),
    Budget = round(runif(1000, min = 5000, max = 20000), 0),
    Channel = sample(c("Email", "Social Media", "Search"), 1000, replace = TRUE),
    Impressions = round(runif(1000, min = 1000, max = 50000), 0),
    Conversions = sample(100:1000, 1000, replace = TRUE)
  )
  return(campaign_data)
}

calculate_campaign_metrics <- function(campaign_data) {
  campaign_data <- campaign_data %>%
    mutate(
      CTR = Conversions / Impressions * 100,
      Conversion_Rate = Conversions / Impressions * 100
    )
  return(campaign_data)
}

convert_columns_to_factors <- function(campaign_data) {
  campaign_data$Group <- as.factor(campaign_data$Group)
  campaign_data$Channel <- as.factor(campaign_data$Channel)
  return(campaign_data)
}

build_regression_model <- function(campaign_data) {
  regression_model <- lm(Conversion_Rate ~ Budget + Channel + Group, data = campaign_data)
  return(regression_model)
}

