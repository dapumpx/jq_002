import datetime
import pandas as pd
from jqdatasdk import *

auth('13816180425','yly0815')

# d = get_security_info('002464.XSHE')

# d = get_concepts()

# d = get_concept_stocks('GN039')

# for stock in d:
#     print(get_security_info(stock).display_name)

# d = get_money_flow(normalize_code('000636'), count=3)

# d = get_billboard_list(normalize_code('000636'), '2018-06-01', '2018-07-02')

d = get_price(normalize_code('000636'), start_date='2017-07-24', end_date='2018-07-03', skip_paused=True, fields=['open', 'close','low','high'])

d.to_csv('result.csv')

exit

print(d)
# print(type(d))

week_open=0
week_close=0
week_low=0
week_high=0
pre_day = None
ds_weekly = {'open':{}, 'close':{}, 'low':{}, 'high':{}}
week_key = None
for key_date in d.index:
    # print(type(key_date))
    # date_obj = key_date.date()
    # print(date_obj.weekday())
    # week_key = key_date
    # print(d.loc[key_date])
    if pre_day is None:pre_day = key_date
    if key_date.date().weekday() <= pre_day.date().weekday():
        if week_high > 0:
            ds_weekly['open'][pre_day] = week_open
            ds_weekly['close'][pre_day] = week_close
            ds_weekly['low'][pre_day] = week_low
            ds_weekly['high'][pre_day] = week_high

        week_open = d.loc[key_date]['open']
        week_close = d.loc[key_date]['close']
        week_low = d.loc[key_date]['low']
        week_high = d.loc[key_date]['high']
    else:
        week_close = d.loc[key_date]['close']
        week_low = min(d.loc[key_date]['low'], week_low)
        week_high = max(d.loc[key_date]['high'], week_high)

    pre_day = key_date

df2_weekly = pd.DataFrame(columns=['open', 'close', 'low', 'high'], data=ds_weekly)
print(df2_weekly)



    