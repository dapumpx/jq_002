import datetime
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import talib
import matplotlib.pyplot as plt
from scipy import special, optimize, signal
# from decimal import Decimal

def ma(df, num):
    result = []
    # num = Decimal(num1)
    for key in df.index:
        date = key
        len_list = len(result)
        if len_list >= num - 1:
            # avg = Decimal(0)
            avg = 0
            # strContent = ''
            count = int(num)
            for i in range(count - 1):
                # avg = avg + Decimal(df.loc[df.index[len_list-i - 1]].close)
                avg = avg + df.loc[df.index[len_list-i - 1]].close
            # avg = avg + Decimal(df.loc[key].close)
            avg = avg + df.loc[key].close
            # print(avg)
            avg = avg / num
            # avg = avg/num
           

            result.append([key, df.loc[key].close, avg])
        else:
            result.append([key, df.loc[key].close, 0])
        
        print(result[len(result)-1])

    

df2 = pd.read_csv('result.csv', index_col=0)
# ma(df2, 5)

# x = np.linspace(-1, 1, 50)
# y = 2*x + 1

# plt.figure()
# plt.plot(x, y)
# plt.show()

# print(df2.close.values)
# list_close = df2.close.values
# ma5=talib.SMA(list_close,timeperiod=5)
# print(ma5)

# print(talib.get_functions())

# print(df2.close.keys)

# def f(x1, c):
#      m1 = np.sin(2*np.pi*x1)
#      m2 = np.exp(-c*x1)
#      return np.multiply(m1, m2)
# x = np.linspace(0,4,100)
# sigma = 0.5

plt.figure()
plt.plot(df2.close.index, df2.close.values, 'r')
a = signal.argrelextrema(df2.close.values, np.greater)
for aa in a:
    plt.plot(df2.close.index[aa], df2.close.values[aa], 'ro')
# plt.plot(x, f(x, sigma), 'r')

ma5=talib.SMA(df2.close.values,timeperiod=5)
plt.plot(df2.close.index, ma5, 'y')

ma10=talib.SMA(df2.close.values,timeperiod=10)
plt.plot(df2.close.index, ma10, 'm--')

plt.show()
