set.seed(123)

campaign_data <- data.frame(
  Group = sample(c("A", "B"), 1000, replace = TRUE),
  Budget = round(runif(1000, min = 5000, max = 20000), 0),
  Channel = sample(c("Email", "Social Media", "Search"), 1000, replace = TRUE),
  Impressions = round(runif(1000, min = 1000, max = 50000), 0),
  Conversions = sample(100:1000, 1000, replace = TRUE)
)

campaign_data <- campaign_data %>%
  mutate(
    CTR = Conversions / Impressions * 100,
    Conversion_Rate = Conversions / Impressions * 100
  )

head(campaign_data)

campaign_data$Group <- as.factor(campaign_data$Group)
campaign_data$Channel <- as.factor(campaign_data$Channel)

regression_model <- lm(Conversion_Rate ~ Budget + Channel + Group, data = campaign_data)

summary(regression_model)
coeftest(regression_model)
