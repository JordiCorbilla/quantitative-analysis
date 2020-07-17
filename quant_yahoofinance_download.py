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
from datetime import datetime

ticker = 'GOOG'
yahoo_financials = YahooFinancials(ticker)
end_date = datetime.today()

historical_stock_prices = yahoo_financials.get_historical_price_data('2004-08-01', end_date.strftime("%Y-%m-%d"), 'weekly')