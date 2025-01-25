if (!require(arules)) install.packages("arules", dependencies = TRUE)

library(arules)

set.seed(123)
n_customers <- 10
n_transactions <- 50

products <- c("Product A", "Product B", "Product C", "Product D", "Product E")
transaction_data <- data.frame(
  customer_id = sample(1:n_customers, n_transactions, replace = TRUE),
  transaction_date = sample(seq.Date(from = as.Date('2022-01-01'), to = Sys.Date(), by = 'day'), n_transactions, replace = TRUE),
  product = sample(products, n_transactions, replace = TRUE)
)

transaction_list <- split(transaction_data$product, transaction_data$customer_id)
transaction_list <- lapply(transaction_list, unique)
transactions <- as(transaction_list, "transactions")

summary(transactions)

rules <- apriori(transactions, parameter = list(support = 0.2, confidence = 0.6, target = "rules"))

inspect(rules)

lift_rules <- subset(rules, lift > 1)
inspect(lift_rules)

library(arulesViz)
plot(rules, method = "graph", main = "Market Basket Analysis - Association Rules")

top_rules <- sort(rules, by = "lift", decreasing = TRUE)
inspect(head(top_rules, 10))
