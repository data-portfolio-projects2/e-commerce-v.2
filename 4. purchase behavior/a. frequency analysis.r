set.seed(123)

n_customers <- 50
n_transactions <- 200

customers <- sample(1:n_customers, n_transactions, replace = TRUE)
product_names <- c("Product_A", "Product_B", "Product_C", "Product_D", "Product_E")
products <- sample(product_names, n_transactions, replace = TRUE)
transaction_dates <- sample(seq.Date(from = as.Date('2023-01-01'), to = as.Date('2023-12-31'), by = 'day'), n_transactions, replace = TRUE)

transaction_data <- data.frame(
  customer_id = customers,
  transaction_date = transaction_dates,
  product = products
)

head(transaction_data)

library(dplyr)

purchase_frequency <- transaction_data %>%
  group_by(customer_id) %>%
  summarise(total_purchases = n())

summary_stats <- summary(purchase_frequency$total_purchases)

transaction_data$month <- format(transaction_data$transaction_date, "%Y-%m")
monthly_purchases <- transaction_data %>%
  group_by(month) %>%
  summarise(monthly_total = n())

library(ggplot2)

ggplot(purchase_frequency, aes(x = customer_id, y = total_purchases)) +
  geom_bar(stat = "identity", fill = "skyblue") +
  theme_minimal() +
  labs(title = "Frequency of Purchases per Customer", x = "Customer ID", y = "Total Purchases")
