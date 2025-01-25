load_required_packages <- function() {
  if (!require(gridExtra)) install.packages("gridExtra", dependencies = TRUE)
  library(gridExtra)
}

perform_chisq_test <- function(table_data) {
  chisq.test(table_data)
}

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

create_donut_plot <- function(data, var, title) {
  ggplot(data, aes(x = 2, fill = {{var}})) +
    geom_bar(width = 1, show.legend = TRUE) +
    coord_polar(theta = "y") +
    labs(title = title) +
    theme_void() +
    theme(legend.position = "bottom")
}

arrange_plots <- function(plot1, plot2, plot3) {
  grid.arrange(plot1, plot2, plot3, ncol = 2, nrow = 2)
}

run_eda <- function(demographics) {
  load_required_packages()
  
  
