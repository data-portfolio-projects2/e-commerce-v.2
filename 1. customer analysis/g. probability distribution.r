library(ggplot2)
library(fitdistrplus)
library(MASS)
library(gridExtra)

fit_age <- fitdist(demographics$Age, "norm")
fit_income <- fitdist(demographics$Income_Level, "norm")
fit_poisson_age <- fitdist(demographics$Age, "pois")
fit_binom_age <- fitdist(demographics$Age, "binom", size = 100, prob = 0.5)

age_normal_plot <- ggplot(demographics, aes(x = Age)) +
  geom_histogram(aes(y = ..density..), bins = 10, fill = "skyblue", color = "black") +
  stat_function(fun = dnorm, args = list(mean = fit_age$estimate["mean"], sd = fit_age$estimate["sd"]),
                color = "red", size = 1) +
  labs(title = "Age Distribution (Normal Fit)", x = "Age", y = "Density") +
  theme_minimal()

income_normal_plot <- ggplot(demographics, aes(x = Income_Level)) +
  geom_histogram(aes(y = ..density..), bins = 10, fill = "skyblue", color = "black") +
  stat_function(fun = dnorm, args = list(mean = fit_income$estimate["mean"], sd = fit_income$estimate["sd"]),
                color = "red", size = 1) +
  labs(title = "Income Distribution (Normal Fit)", x = "Income Level", y = "Density") +
  theme_minimal()

poisson_age_plot <- ggplot(demographics, aes(x = Age)) +
  geom_histogram(aes(y = ..density..), bins = 10, fill = "skyblue", color = "black") +
  stat_function(fun = dpois, args = list(lambda = fit_poisson_age$estimate["lambda"]),
                color = "red", size = 1) +
  labs(title = "Age Distribution (Poisson Fit)", x = "Age", y = "Density") +
  theme_minimal()

binom_age_plot <- ggplot(demographics, aes(x = Age)) +
  geom_histogram(aes(y = ..density..), bins = 10, fill = "skyblue", color = "black") +
  stat_function(fun = dbinom, args = list(size = 100, prob = 0.5),
                color = "red", size = 1) +
  labs(title = "Age Distribution (Binomial Fit)", x = "Age", y = "Density") +
  theme_minimal()

grid.arrange(age_normal_plot, income_normal_plot, poisson_age_plot, binom_age_plot, ncol = 2)

cat("\nNormal Fit for Age:")
print(fit_age)
cat("\nNormal Fit for Income:")
print(fit_income)
cat("\nPoisson Fit for Age:")
print(fit_poisson_age)
cat("\nBinomial Fit for Age:")
print(fit_binom_age)
