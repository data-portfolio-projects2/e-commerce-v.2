if (!require(gridExtra)) install.packages("gridExtra", dependencies = TRUE)
library(gridExtra)

gender_location_table <- table(demographics$Gender, demographics$Location)
gender_location_test <- chisq.test(gender_location_table)

location_cluster_table <- table(demographics$Location, demographics$Cluster)
location_cluster_test <- chisq.test(location_cluster_table)

create_bar_plot <- function(data, x_var, fill_var, title, x_lab, y_lab, test_stat, test_df, test_pvalue) {
  ggplot(data, aes(x = {{x_var}}, fill = {{fill_var}})) +
    geom_bar(position = "dodge") +
    labs(title = title, x = x_lab, y = y_lab) +
    theme_minimal() +
    annotate("text", x = 1.5, y = 6, 
             label = paste("Chi-squared = ", round(test_stat, 2),
                           "\ndf = ", test_df,
                           "\np-value = ", round(test_pvalue, 4)),
             size = 3, hjust = 0.5)
}

gender_location_plot <- create_bar_plot(
  demographics, Location, Gender, "Gender vs. Location", "Location", "Count", 
  gender_location_test$statistic, gender_location_test$parameter, gender_location_test$p.value
)

location_cluster_plot <- create_bar_plot(
  demographics, Cluster, Location, "Location vs. Cluster", "Cluster", "Count", 
  location_cluster_test$statistic, location_cluster_test$parameter, location_cluster_test$p.value
)

gender_location_donut_plot <- ggplot(demographics, aes(x = 2, fill = Gender)) +
  geom_bar(width = 1, show.legend = TRUE) +
  coord_polar(theta = "y") +
  labs(title = "Gender Distribution in Location") +
  theme_void() +
  theme(legend.position = "bottom")

grid.arrange(gender_location_plot, location_cluster_plot, gender_location_donut_plot, ncol = 2, nrow = 2)
