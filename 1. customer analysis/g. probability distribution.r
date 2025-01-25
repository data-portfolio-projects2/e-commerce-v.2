load_required_packages <- function() {
  library(ggplot2)
  library(fitdistrplus)
  library(MASS)
  library(gridExtra)
}

fit_distributions <- function(data) {
  fit_age <- fitdist(data$Age, "norm")
  fit_income <- fitdist(data$Income_Level, "norm")
  fit_poisson_age <- fitdist(data$Age, "pois")
  fit_binom_age <- fitdist(data$Age, "binom", size = 100, prob = 0.5)
  
  list(fit_age, fit_income, fit_poisson_age, fit_binom_age)
}

create_histogram_plot <- function(data, dist_type, dist_fit, dist_args, title, x_lab, y_lab) {
  ggplot(data, aes(x = {{dist_type}})) +
    geom_histogram(aes(y = ..density..), bins = 10, fill = "skyblue", color = "black") +
    stat_function(fun = {{dist_args}}$fun, args = dist_args$args,
                  color = "red", size = 1) +
    labs(title = title, x = x_lab, y = y_lab) +
    theme_minimal()
}

arrange_and_display_plots <- function(age_normal_plot, income_normal_plot, poisson_age_plot, binom_age_plot) {
  grid.arrange(age_normal_plot, income_normal_plot, poisson_age_plot, binom_age_plot, ncol = 2)
}

display_distribution_fits <- function(fit_age, fit_income, fit_poisson_age, fit_binom_age) {
  cat("\nNormal Fit for Age:")
  print(fit_age)
  cat("\nNormal Fit for Income:")
  print(fit_income)
  cat("\nPoisson Fit for Age:")
  print(fit_poisson_age)
  cat("\nBinomial Fit for Age:")
  print(fit_binom_age)
}
