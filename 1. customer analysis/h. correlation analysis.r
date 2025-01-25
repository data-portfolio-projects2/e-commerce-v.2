calculate_correlation <- function(data) {
  cor(data$Age, data$Income_Level)
}

create_correlation_plot <- function(data) {
  ggplot(data, aes(x = Age, y = Income_Level)) +
    geom_point(color = "blue", size = 3) +
    geom_smooth(method = "lm", color = "red", linetype = "dashed") + 
    labs(title = "Correlation Between Age and Income Level", x = "Age", y = "Income Level") +
    theme_minimal()
}

display_correlation_result <- function(correlation_result) {
  cat("\nCorrelation between Age and Income Level:", correlation_result)
}
