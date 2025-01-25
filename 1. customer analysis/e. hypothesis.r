library(ggplot2)
library(gridExtra)

income_by_gender_ttest <- t.test(Income_Level ~ Gender, data = demographics)
age_by_location_anova <- aov(Age ~ Location, data = demographics)

t_test_results <- paste("T-test Results: \n", 
                        "T-statistic = ", round(income_by_gender_ttest$statistic, 2), "\n", 
                        "p-value = ", round(income_by_gender_ttest$p.value, 4))

anova_results <- summary(age_by_location_anova)

income_gender_plot <- ggplot(demographics, aes(x = Gender, y = Income_Level, fill = Gender)) +
  geom_boxplot() +
  labs(title = "Income by Gender", x = "Gender", y = "Income Level") +
  theme_minimal()

age_location_plot <- ggplot(demographics, aes(x = Location, y = Age, fill = Location)) +
  geom_boxplot() +
  labs(title = "Age by Location", x = "Location", y = "Age") +
  theme_minimal()

grid.arrange(income_gender_plot, age_location_plot, ncol = 2, nrow = 1)
print(t_test_results)
print(anova_results)
