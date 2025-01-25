library(forecast)
library(tseries)

generate_sales_data <- function() {
  set.seed(123)
  data.frame(
    date = seq.Date(from = as.Date('2022-01-01'), by = 'day', length.out = 180),
    sales = rnorm(180, mean = 200, sd = 50) + sin(1:180/10) * 50
  )
}

plot_sales_data <- function(sales_data) {
  ggplot(sales_data, aes(x = date, y = sales)) +
    geom_line() +
    ggtitle("Simulated Sales Data") +
    xlab("Date") +
    ylab("Sales") +
    theme_minimal()
}

convert_to_time_series <- function(sales_data) {
  ts(sales_data$sales, frequency = 365)
}

decompose_sales <- function(sales_ts) {
  decompose(sales_ts)
}

perform_adf_test <- function(sales_ts) {
  adf.test(sales_ts)
}

apply_differencing <- function(sales_ts) {
  diff(sales_ts, differences = 1)
}

fit_arima_model <- function(sales_ts) {
  auto.arima(sales_ts)
}

forecast_sales_data <- function(arima_model) {
  forecast(arima_model, h = 30)
}

plot_forecast <- function(forecast_sales) {
  plot(forecast_sales, main = "Sales Forecast (Next 30 Days)")
}

plot_seasonal_component <- function(sales_data, seasonal_component) {
  ggplot(data = sales_data, aes(x = date, y = seasonal_component)) +
    geom_line() +
    ggtitle("Seasonal Component of Sales") +
    xlab("Date") +
    ylab("Seasonality Effect") +
    theme_minimal()
}

