import pandas as pd


colnames = ['time', 'T', 'phi', 'ws','wd', 'wg', 'prec', 'pres', 'bat', 'vwc','period']

df =  pd.read_csv('Meteo_1min_2017_raw1.dat', usecols = colnames, low_memory = False,
                 index_col ='time',  parse_dates = True, dayfirst = False)

df = df[~df.index.duplicated(keep='first')]# dumps duplicates

# creates 1-min timeseries
first = df.iloc[0].name
last = df.iloc[-1].name
dr = pd.date_range(first, last, freq = '1min', name = 'Time')
df = df.reindex(dr)

print(df.head())
class Size():
    '''Meteorological size measured by  LAPUP Meteo station'''
    sizelist = []
    def __init__(self, col, name, min_value, max_value):
        self.col = col
        self.name = name
        self.min_value = min_value
        self.max_value = max_value
        Size.sizelist.append(self)

Size('T', 'Temperature',-2.0, 41.0)
Size('phi','Relative humidity', 5.0, 100.0)
Size('prec','Precipitation', 0.0, 40.0)
Size('pres', 'Pressure', 970.0, 1030.0)
Size('bat', 'Battery voltage', 9.0, 15.0)
Size('ws', 'Wind speed', 0.0, 75.0)
Size('wg', 'Wind gust', 0.0, 40.0)

s = Size.sizelist
for i in s:
    print(i.col, i.name, i.min_value, i.max_value,sep = '\t')