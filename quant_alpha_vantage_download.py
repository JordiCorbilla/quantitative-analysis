# -*- coding: utf-8 -*-
# Created on Sun Jul 19 18:10:11 2020
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
from alpha_vantage.timeseries import TimeSeries
import pandas as pd
import time as time

KEY = 'yourkeyhere!'

# Define output_format as pandas, otherwise we'll get the data in JSON format
ts = TimeSeries(key=KEY, output_format='pandas')
data = ts.get_daily('TSLA', outputsize='full')[0]
data.columns = ['open', 'high', 'low', 'close', 'volume']
# Data comes sorted by date desc and we need to reverse it
data = data.iloc[::-1]

stocks = ["TSLA", "AMZN", "GOOG", "MSFT", "FB", "ES=F", "CABK.MC"]
close_price = pd.DataFrame()

# To overcome the API call frequency limitation, we need to make our query slower
number_api_calls = 0
for symbol_ticker in stocks:
    start_time = time.time()
    ts = TimeSeries(key=KEY, output_format='pandas')
    data = ts.get_intraday(symbol=symbol_ticker, interval='1min', outputsize='full')[0]
    number_api_calls += 1
    data.columns = ['open', 'high', 'low', 'close', 'volume']
    close_price[symbol_ticker] = data['close']
    if number_api_calls == 5:
        number_api_calls = 0
        time.sleep(60 - ((time.time() - start_time) % 60.0))
        