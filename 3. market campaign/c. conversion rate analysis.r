library(ggplot2)

ggplot(campaign_data, aes(x = Group, y = Conversion_Rate, fill = Group)) +
  geom_boxplot() +
  labs(title = "Conversion Rate by Group (A vs B)", x = "Group", y = "Conversion Rate (%)") +
  theme_minimal()

ggplot(campaign_data, aes(x = Channel, y = Conversion_Rate, fill = Channel)) +
  geom_boxplot() +
  labs(title = "Conversion Rate by Marketing Channel", x = "Channel", y = "Conversion Rate (%)") +
  theme_minimal()
