set.seed(123)

n_customers <- 10
n_transactions <- 50

transaction_data <- data.frame(
  customer_id = sample(1:n_customers, n_transactions, replace = TRUE),
  transaction_date = sample(seq.Date(from = as.Date('2022-01-01'), to = Sys.Date(), by = 'day'), n_transactions, replace = TRUE),
  amount_spent = sample(50:500, n_transactions, replace = TRUE)
)

purchase_frequency <- transaction_data %>%
  group_by(customer_id) %>%
  summarise(total_purchases = n())

recency_data <- transaction_data %>%
  group_by(customer_id) %>%
  summarise(most_recent_purchase = max(transaction_date)) %>%
  mutate(recency_days = as.integer(Sys.Date() - most_recent_purchase))

monetary_data <- transaction_data %>%
  group_by(customer_id) %>%
  summarise(total_spent = sum(amount_spent))

rfm_data <- purchase_frequency %>%
  left_join(recency_data, by = "customer_id") %>%
  left_join(monetary_data, by = "customer_id")

rfm_kmeans <- kmeans(rfm_data[, c("recency_days", "total_purchases", "total_spent")], centers = 3)

rfm_data$cluster <- rfm_kmeans$cluster

library(ggplot2)

ggplot(rfm_data, aes(x = total_purchases, y = total_spent, color = factor(cluster))) +
  geom_point(size = 3) +
  theme_minimal() +
  labs(title = "RFM Customer Segments", x = "Frequency (Total Purchases)", y = "Monetary (Total Spent)", color = "Cluster")

rfm_data$segment <- case_when(
  rfm_data$cluster == 1 ~ "High-Value",
  rfm_data$cluster == 2 ~ "Low-Value",
  rfm_data$cluster == 3 ~ "At-Risk"
)

head(rfm_data)
summary(rfm_data)
