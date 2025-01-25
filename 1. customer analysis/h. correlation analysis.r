correlation_result <- cor(demographics$Age, demographics$Income_Level)

cat("\nCorrelation between Age and Income Level:", correlation_result)

correlation_plot <- ggplot(demographics, aes(x = Age, y = Income_Level)) +
  geom_point(color = "blue", size = 3) +
  geom_smooth(method = "lm", color = "red", linetype = "dashed") + 
  labs(title = "Correlation Between Age and Income Level", x = "Age", y = "Income Level") +
  theme_minimal()

print(correlation_plot)
