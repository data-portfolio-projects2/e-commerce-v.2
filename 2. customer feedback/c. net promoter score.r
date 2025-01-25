set_seed_and_generate_ratings <- function() {
  set.seed(123)
  n <- 100
  ratings <- sample(0:10, n, replace = TRUE)
  return(ratings)
}

create_nps_data <- function(ratings) {
  nps_data <- data.frame(
    Customer = paste("Customer", 1:length(ratings)),
    Rating = ratings
  )
  nps_data$Category <- ifelse(nps_data$Rating >= 9, "Promoter",
                               ifelse(nps_data$Rating >= 7, "Passive", "Detractor"))
  return(nps_data)
}

calculate_nps_score <- function(nps_data) {
  promoters_percentage <- sum(nps_data$Category == "Promoter") / nrow(nps_data) * 100
  detractors_percentage <- sum(nps_data$Category == "Detractor") / nrow(nps_data) * 100
  nps_score <- promoters_percentage - detractors_percentage
  return(nps_score)
}

visualize_nps <- function(nps_data) {
  ggplot(nps_data, aes(x = Category)) +
    geom_bar(fill = c("green", "yellow", "red")) +
    labs(title = "Net Promoter Score (NPS) Categories", x = "Category", y = "Count") +
    theme_minimal()
}
