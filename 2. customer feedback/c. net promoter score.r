set.seed(123)
n <- 100
ratings <- sample(0:10, n, replace = TRUE)

nps_data <- data.frame(
  Customer = paste("Customer", 1:n),
  Rating = ratings
)

nps_data$Category <- ifelse(nps_data$Rating >= 9, "Promoter",
                             ifelse(nps_data$Rating >= 7, "Passive", "Detractor"))

promoters_percentage <- sum(nps_data$Category == "Promoter") / n * 100
detractors_percentage <- sum(nps_data$Category == "Detractor") / n * 100
nps_score <- promoters_percentage - detractors_percentage

cat("NPS Score:", nps_score, "\n")

ggplot(nps_data, aes(x = Category)) +
  geom_bar(fill = c("green", "yellow", "red")) +
  labs(title = "Net Promoter Score (NPS) Categories", x = "Category", y = "Count") +
  theme_minimal()
