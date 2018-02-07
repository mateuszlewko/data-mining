require("xts")
library("TTR")
library("forecast")

data <- read.csv(file="data.csv", header=TRUE, sep=";")
# dates <- as.POSIXct(data$Date, format="%Y-%m-%d")
# data <- xts(data, order.by=dates) 
data

plotForecastErrors <- function(forecasterrors)
{
  # make a histogram of the forecast errors:
  mybinsize <- IQR(forecasterrors)/4
  mysd   <- sd(forecasterrors)
  mymin  <- min(forecasterrors) - mysd*5
  mymax  <- max(forecasterrors) + mysd*3
  # generate normally distributed data with mean 0 and standard deviation mysd
  mynorm <- rnorm(10000, mean=0, sd=mysd)
  mymin2 <- min(mynorm)
  mymax2 <- max(mynorm)
  if (mymin2 < mymin) { mymin <- mymin2 }
  if (mymax2 > mymax) { mymax <- mymax2 }
  # make a red histogram of the forecast errors, with the normally distributed data overlaid:
  mybins <- seq(mymin, mymax, mybinsize)
  hist(forecasterrors, col="red", freq=FALSE, breaks=mybins)
  # freq=FALSE ensures the area under the histogram = 1
  # generate normally distributed data with mean 0 and standard deviation mysd
  myhist <- hist(mynorm, plot=FALSE, breaks=mybins)
  # plot the normal curve as a blue line on top of the histogram of forecast errors:
  points(myhist$mids, myhist$density, type="l", col="blue", lwd=2)
}

analysis <- function(name) 
{
  stock <- unlist(subset(data, Name==name, select=C))
  # print(stock)
  
  stock_ts <- ts(stock)
  # print(stock_ts)
  
  plot.ts(stock_ts)
  plot.ts(SMA(stock_ts, n=180))
  
  # decompose(stock_ts)
  
  print("HoltWinters:")
  hw <- HoltWinters(stock_ts, beta=FALSE, gamma=FALSE)
  print(hw)
  print(head(hw$fitted))
  
  print("SSE:")
  print(hw$SSE)
  
  plot(hw)
  
  hw_forecast = forecast(stock_ts, h=20)
  plot(hw_forecast)
  
  print(acf(hw_forecast$residuals, lag.max=20))
  print(Box.test(hw_forecast$residuals, lag=20, type="Ljung-Box"))

  plot.ts(hw_forecast$residuals)  
  plotForecastErrors(hw_forecast$residuals)
  
  hw2 <- HoltWinters(stock_ts, gamma=FALSE)
  print(hw2$SSE)
  plot(hw2)
  
  stock_ts_diff <- diff(stock_ts, differences=1)
  plot.ts(stock_ts_diff)
  
  acf(stock_ts_diff, lag.max=20)
  print(acf(stock_ts_diff, lag.max=20, plot=FALSE))
  pacf(stock_ts_diff, lag.max=20)
  print(pacf(stock_ts_diff, lag.max=20, plot=FALSE))

  print(auto.arima(stock_ts))
  
  stock_arima <- arima(stock_ts, order=c(1, 1, 1))
  print(stock_arima)
  
  stock_forecast_arima <- forecast(stock_arima, h=120)
  plot(stock_forecast_arima)
}

# analysis("CYFRPLSAT")
# analysis("KGHM")
# analysis("JSW")
analysis("BZWBK")
