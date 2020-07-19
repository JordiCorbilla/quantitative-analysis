# -*- coding: utf-8 -*-
# Created on Thu Jul 16 21:13:52 2020
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

import yfinance as yf
import json
import pandas as pd
from datetime import datetime, timedelta

sec = yf.Ticker("TSLA")
data = yf.download("TSLA", period="1y")

print('Info')
print(json.dumps(sec.info, indent=4, sort_keys=True))

stocks = ["TSLA", "AMZN", "GOOG", "MSFT", "FB", "ES=F", "CABK.MC"]
start_date = datetime.today()-timedelta(30)
end_date = datetime.today()
close_price = pd.DataFrame()
adjusted_close_price = pd.DataFrame()

for symbol_ticker in stocks:
    downloaded_data = yf.download(symbol_ticker, start_date, end_date)
    close_price[symbol_ticker] = downloaded_data['Close']
    adjusted_close_price[symbol_ticker] = downloaded_data['Adj Close']