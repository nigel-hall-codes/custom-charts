import mpl_finance as mplf
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime


def plot(df1):
    df1['Date'] = mdates.date2num(df1.index)
    f1 = plt.subplot2grid((6, 4), (1, 0), rowspan=6, colspan=4)
    mplf.candlestick_ohlc(f1, zip(df1['Date'], df1['Open'], df1['High'], df1['Low'], df1['Close']),
                          width=.5 / (24 * 60), colorup='#53c156', colordown='#ff1717')

    f1.xaxis_date()
    f1.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d %H:%M'))
    plt.xticks(rotation=45)
    plt.ylabel('Price')
    plt.xlabel('Date Hours:Minutes')
    plt.show()


def from_dates(date_start, date_end, df):
    df['Date'] = df.index
    df = df.loc[(df['Date'] >= date_start) & (df['Date'] <= date_end)]
    plot(df)



def from_date_minus_delta_minutes(df, end, minutes):
    df['Date'] = df.index
    end = datetime.datetime.strptime(end, "%Y-%m-%d %H:%M:%S")
    date_start = end - datetime.timedelta(minutes=minutes)
    from_dates(date_start,end,df)




