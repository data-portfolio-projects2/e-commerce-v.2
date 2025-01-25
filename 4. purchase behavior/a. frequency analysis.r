set.seed(123)

generate_transaction_data <- function(n_customers, n_transactions) {
  customers <- sample(1:n_customers, n_transactions, replace = TRUE)
  product_names <- c("Product_A", "Product_B", "Product_C", "Product_D", "Product_E")
  products <- sample(product_names, n_transactions, replace = TRUE)
  transaction_dates <- sample(seq.Date(from = as.Date('2023-01-01'), to = as.Date('2023-12-31'), by = 'day'), n_transactions, replace = TRUE)
  
  data.frame(
    customer_id = customers,
    transaction_date = transaction_dates,
    product = products
  )
}

summarize_purchase_frequency <- function(transaction_data) {
  transaction_data %>%
    group_by(customer_id) %>%
    summarise(total_purchases = n())
}

summarize_monthly_purchases <- function(transaction_data) {
  transaction_data$month <- format(transaction_data$transaction_date, "%Y-%m")
  transaction_data %>%
    group_by(month) %>%
    summarise(monthly_total = n())
}

plot_purchase_frequency <- function(purchase_frequency) {
  ggplot(purchase_frequency, aes(x = customer_id, y = total_purchases)) +
    geom_bar(stat = "identity", fill = "skyblue") +
    theme_minimal() +
    labs(title = "Frequency of Purchases per Customer", x = "Customer ID", y = "Total Purchases")
}

