# ML_2020_project_Group-30

In our report, we replicated algorithm BHT-ARIMA proposing in the paper ``Block Hankel Tensor ARIMA for Multiple Short Time Series Forecasting". This method used for multivariate time-series (TS) forecasting using Hankelization and Tucker Decomposition. We measured the forecasting accuracy using the Normalized Root Mean Error metric. In time series forecasting topic BHT-ARIMA method performs strong results compare with traditional benchmarks (ARIMA, XGBoost, Prophet, DeepAR, etc).

## Datasets description
We tested BHT-ARIMA on 3 public from the paper ``Block Hankel Tensor ARIMA for Multiple Short Time Series Forecasting''. They're called Traffic, Electricity, Smoke Video. 

Traffic data describes traffic on the Los Angeles County highway network. We use the subset, which randomly selects 228 sensors, and combines it into a daily interval for each TS with data points of 80 days.

Electricity records 321 hourly electricity consumption by customers. We took every 24-time points to get a daily TS data set of 321 x 1096.

Smoke Video records smoke from the chimney of the plant. We sample and resize the images to get a third-order TS data set of 36 x 64 x 100.

And also we used two external datasets: 

In M4 (https://github.com/Mcompetitions/M4-methods/tree/master/Dataset) there are different TS datasets, such as Micro, Industry, Finance, etc, for different frequencies, such as daily data, monthly data, quarterly data, etc.

M5 (https://www.kaggle.com/c/m5-forecasting-accuracy/data) contains information about the dates on which the products are sold, the historical daily unit sales data per product and the store, information about the price of the products sold per store and date.

## Paper
- **"[Block Hankel Tensor ARIMA for Multiple Short Time Series Forecasting](https://arxiv.org/abs/2002.12135)", AAAI-20**

## Report
## Presentation



