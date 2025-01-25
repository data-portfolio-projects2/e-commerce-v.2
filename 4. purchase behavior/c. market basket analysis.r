library(arules)

generate_transaction_data <- function(n_customers, n_transactions, products) {
  data.frame(
    customer_id = sample(1:n_customers, n_transactions, replace = TRUE),
    transaction_date = sample(seq.Date(from = as.Date('2022-01-01'), to = Sys.Date(), by = 'day'), n_transactions, replace = TRUE),
    product = sample(products, n_transactions, replace = TRUE)
  )
}

create_transaction_list <- function(transaction_data) {
  transaction_list <- split(transaction_data$product, transaction_data$customer_id)
  lapply(transaction_list, unique)
}

convert_to_transactions <- function(transaction_list) {
  as(transaction_list, "transactions")
}

generate_association_rules <- function(transactions) {
  apriori(transactions, parameter = list(support = 0.2, confidence = 0.6, target = "rules"))
}

filter_rules_by_lift <- function(rules) {
  subset(rules, lift > 1)
}

visualize_rules <- function(rules) {
  library(arulesViz)
  plot(rules, method = "graph", main = "Market Basket Analysis - Association Rules")
}

