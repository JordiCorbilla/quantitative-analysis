# -*- coding: utf-8 -*-
# Created on Fri Jul 17 19:42:23 2020
# 
# Copyright 2020 Jordi Corbilla. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

from yahoofinancials import YahooFinancials
import pandas as pd
from datetime import datetime, timedelta

ticker = 'GOOG'
yahoo_financials = YahooFinancials(ticker)
end_date = datetime.today()

historical_stock_prices = yahoo_financials.get_historical_price_data('2004-08-01', end_date.strftime("%Y-%m-%d"), 'weekly')

# Downloading multiple tickers

start_date = datetime.today()-timedelta(30)
stocks = ["TSLA", "AMZN", "GOOG", "MSFT", "FB", "ES=F", "CABK.MC"]
close_price = pd.DataFrame()
adjusted_close_price = pd.DataFrame()

for symbol_ticker in stocks:
    yahoo_financials = YahooFinancials(symbol_ticker)
    # no intraday option possible for yahoo financials library
    historical_stock_prices = yahoo_financials.get_historical_price_data(start_date.strftime("%Y-%m-%d"), end_date.strftime("%Y-%m-%d"), 'daily')
    prices = historical_stock_prices[symbol_ticker]['prices']
    # Define a DataFrame out of the JSON
    prices_to_dataframe = pd.DataFrame(prices)[['formatted_date', 'close', 'adjclose']]
    # Specify the time series as the index
    prices_to_dataframe.set_index('formatted_date', inplace=True)
    # Remove all missing values Na*
    prices_to_dataframe.dropna(inplace=True)
    close_price[symbol_ticker] = prices_to_dataframe['close']
    adjusted_close_price[symbol_ticker] = prices_to_dataframe['adjclose']
