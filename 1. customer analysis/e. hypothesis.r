load_required_packages <- function() {
  library(ggplot2)
  library(gridExtra)
}

perform_t_test <- function(data) {
  t.test(Income_Level ~ Gender, data = data)
}

perform_anova <- function(data) {
  aov(Age ~ Location, data = data)
}

format_test_results <- function(t_test, anova) {
  t_test_results <- paste("T-test Results: \n", 
                          "T-statistic = ", round(t_test$statistic, 2), "\n", 
                          "p-value = ", round(t_test$p.value, 4))
  
  anova_results <- summary(anova)
  
  list(t_test_results = t_test_results, anova_results = anova_results)
}

create_income_gender_plot <- function(data) {
  ggplot(data, aes(x = Gender, y = Income_Level, fill = Gender)) +
    geom_boxplot() +
    labs(title = "Income by Gender", x = "Gender", y = "Income Level") +
    theme_minimal()
}

create_age_location_plot <- function(data) {
  ggplot(data, aes(x = Location, y = Age, fill = Location)) +
    geom_boxplot() +
    labs(title = "Age by Location", x = "Location", y = "Age") +
    theme_minimal()
}

arrange_and_display_plots <- function(plot1, plot2) {
  grid.arrange(plot1, plot2, ncol = 2, nrow = 1)
}

perform_eda <- function(data) {
  load_required_packages()
  

