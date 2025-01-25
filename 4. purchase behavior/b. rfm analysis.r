set.seed(123)

generate_transaction_data <- function(n_customers, n_transactions) {
  data.frame(
    customer_id = sample(1:n_customers, n_transactions, replace = TRUE),
    transaction_date = sample(seq.Date(from = as.Date('2022-01-01'), to = Sys.Date(), by = 'day'), n_transactions, replace = TRUE),
    amount_spent = sample(50:500, n_transactions, replace = TRUE)
  )
}

calculate_purchase_frequency <- function(transaction_data) {
  transaction_data %>%
    group_by(customer_id) %>%
    summarise(total_purchases = n())
}

calculate_recency <- function(transaction_data) {
  transaction_data %>%
    group_by(customer_id) %>%
    summarise(most_recent_purchase = max(transaction_date)) %>%
    mutate(recency_days = as.integer(Sys.Date() - most_recent_purchase))
}

calculate_monetary_value <- function(transaction_data) {
  transaction_data %>%
    group_by(customer_id) %>%
    summarise(total_spent = sum(amount_spent))
}

merge_rfm_data <- function(purchase_frequency, recency_data, monetary_data) {
  purchase_frequency %>%
    left_join(recency_data, by = "customer_id") %>%
    left_join(monetary_data, by = "customer_id")
}

perform_kmeans_clustering <- function(rfm_data, centers = 3) {
  kmeans(rfm_data[, c("recency_days", "total_purchases", "total_spent")], centers = centers)
}

assign_customer_segments <- function(rfm_data, kmeans_result) {
  rfm_data$cluster <- kmeans_result$cluster
  rfm_data$segment <- case_when(
    rfm_data$cluster == 1 ~ "High-Value",
    rfm_data$cluster == 2 ~ "Low-Value",
    rfm_data$cluster == 3 ~ "At-Risk"
  )
  rfm_data
}

visualize_rfm_clusters <- function(rfm_data) {
  ggplot(rfm_data, aes(x = total_purchases, y = total_spent, color = factor(cluster))) +
    geom_point(size = 3) +
    theme_minimal() +
    labs(title = "RFM Customer Segments", x = "Frequency (Total Purchases)", y = "Monetary (Total Spent)", color = "Cluster")
}

