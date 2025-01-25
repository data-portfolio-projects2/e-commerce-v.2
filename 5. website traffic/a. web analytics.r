set.seed(123)

traffic_data <- data.frame(
  date = seq.Date(from = as.Date("2023-01-01"), by = "day", length.out = 180),
  page_views = sample(500:2000, 180, replace = TRUE),
  sessions = sample(300:1500, 180, replace = TRUE),
  unique_visitors = sample(200:1200, 180, replace = TRUE)
)

library(dplyr)

stats_summary <- traffic_data %>%
  summarise(
    mean_page_views = mean(page_views),
    median_page_views = median(page_views),
    sd_page_views = sd(page_views),
    mean_sessions = mean(sessions),
    median_sessions = median(sessions),
    sd_sessions = sd(sessions),
    mean_unique_visitors = mean(unique_visitors),
    median_unique_visitors = median(unique_visitors),
    sd_unique_visitors = sd(unique_visitors)
  )

print(stats_summary)

library(ggplot2)

traffic_data_weekly <- traffic_data %>%
  mutate(week = as.numeric(format(date, "%U"))) %>%
  group_by(week) %>%
  summarise(
    weekly_page_views = sum(page_views),
    weekly_sessions = sum(sessions),
    weekly_unique_visitors = sum(unique_visitors)
  )

ggplot(traffic_data_weekly, aes(x = week)) +
  geom_line(aes(y = weekly_page_views, color = "Page Views")) +
  geom_line(aes(y = weekly_sessions, color = "Sessions")) +
  geom_line(aes(y = weekly_unique_visitors, color = "Unique Visitors")) +
  labs(
    title = "Weekly Trends of Website Traffic",
    x = "Week Number",
    y = "Count",
    color = "Metrics"
  ) +
  theme_minimal()
