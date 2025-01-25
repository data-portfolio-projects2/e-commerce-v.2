library(dplyr)

summary_stats <- campaign_data %>%
  summarise(
    Mean_Conversion_Rate = mean(Conversion_Rate),
    Median_Conversion_Rate = median(Conversion_Rate),
    SD_Conversion_Rate = sd(Conversion_Rate),
    Mean_Budget = mean(Budget),
    Median_Budget = median(Budget),
    SD_Budget = sd(Budget),
    Mean_CTR = mean(CTR),
    SD_CTR = sd(CTR)
  )

cat("Descriptive Statistics:\n")

