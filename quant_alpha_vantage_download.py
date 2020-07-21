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

ts = TimeSeries(key='yourkeyhere!', output_format='pandas')
data = ts.get_daily('TSLA', outputsize='full')[0]
data.columns = ['open','high', 'low', 'close', 'volume']