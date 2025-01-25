library(forecast)
library(tseries)
library(ggplot2)

set.seed(123)
sales_data <- data.frame(
  date = seq.Date(from = as.Date('2022-01-01'), by = 'day', length.out = 180),
  sales = rnorm(180, mean = 200, sd = 50) + sin(1:180/10) * 50
)

ggplot(sales_data, aes(x = date, y = sales)) +
  geom_line() +
  ggtitle("Simulated Sales Data") +
  xlab("Date") +
  ylab("Sales") +
  theme_minimal()

sales_ts <- ts(sales_data$sales, frequency = 365)

decomposed_sales <- decompose(sales_ts)
plot(decomposed_sales)

adf_test <- adf.test(sales_ts)
print(adf_test)

if(adf_test$p.value > 0.05) {
  sales_ts <- diff(sales_ts, differences = 1)
}

arima_model <- auto.arima(sales_ts)
forecast_sales <- forecast(arima_model, h = 30)

plot(forecast_sales, main = "Sales Forecast (Next 30 Days)")

seasonal_component <- decomposed_sales$seasonal
ggplot(data = sales_data, aes(x = date, y = seasonal_component)) +
  geom_line() +
  ggtitle("Seasonal Component of Sales") +
  xlab("Date") +
  ylab("Seasonality Effect") +
  theme_minimal()

print(forecast_sales)
