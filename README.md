# custom-charts
Uses mpl_finance library to produce 1 min increment candlestick charts

## Examples

candlestick1m.plot(df)

  Params:
  
    df: pandas DataFrame, contains cols ["Date", "Open", "High", "Low", "Close"]
    
candlestick1m.from_dates(date_start, date_end, df)
  Params:
    date_start: str(datetime) format="%m-%d %H:%M"
    date_end: str(datetime) format="%m-%d %H:%M"
    df: pandas DataFrame, contains cols ["Date", "Open", "High", "Low", "Close"]
    
    
candlestick1m.from_date_minus_delta_minutes(df, end, minutes)
  Params:
    date_end: str(datetime) format="%m-%d %H:%M"
    df: pandas DataFrame, contains cols ["Date", "Open", "High", "Low", "Close"]
    minutes: int
    
