import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import os

tickers = ["AAPL", "NVDA", "MSFT", "SPY", "URTH"]
data = yf.download(tickers, start="2015-01-01", end="2025-01-01", auto_adjust=True)

#print(data.head())

"""
Checks to see if the table can be worked on

data.to_html(r"C:\\Users\\Diego\\Documents\\ProyectoInversion\\dumbumbomba.html")

print(data.isna().sum()) #Check if there are null values

print(data.index.duplicated().sum()) #Chek if there are some duplicated dates

print(data.index.is_monotonic_increasing) #Chek if the order of the dates is correct

huecos = data.index.to_series().diff()
huecos[huecos > pd.Timedelta(days=7)]
"""

# Dividimos la tabla multiIndex en 5 dataframes distintos, uno por índice.
tickers = ["AAPL", "NVDA", "MSFT", "SPY", "URTH"]
datos_concretos = {}
os.makedirs("./ind_data", exist_ok=True)

dir_script = os.path.dirname(os.path.abspath(__file__))
folder_data = os.path.join(dir_script, "ind_data")
os.makedirs(folder_data, exist_ok=True)

for ticker in tickers:
    datos_concretos[ticker] = data.xs(ticker, level=1, axis=1)

    datos_concretos[ticker].to_csv(os.path.join(folder_data, f"{ticker}.csv"))

"""
Si quisieramos visualizar los ultimos valores (de cierre en este caso) de determinada compañia:
aapl = pd.read_csv(os.path.join(folder_data, "AAPL.csv"), index_col=0, parse_dates=True)

aapl["Close"].plot()
plt.show()
"""

for ticker in tickers:
    tickerdf = pd.read_csv(os.path.join(folder_data, f"{ticker}.csv"), index_col=0, parse_dates=True)
    normalizado = tickerdf["Close"] / tickerdf["Close"].iloc[0] * 100 # Normalizamos 
    normalizado.plot(label=ticker)

    
plt.legend()
plt.yscale("log") #Ponemos escala logarítmica para que el crecimiento de Nvidia no deje a las demás tan bajas
plt.show()