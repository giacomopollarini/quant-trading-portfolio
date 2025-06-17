import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# Scarica dati EUR/USD
data = yf.download('EURUSD=X', start='2023-01-01', end='2024-01-01')

# Calcola medie mobili
data['SMA50'] = data['Close'].rolling(window=50).mean()
data['SMA200'] = data['Close'].rolling(window=200).mean()

# Segnale: long se SMA50 > SMA200, short se SMA50 < SMA200
data['Position'] = 0
data.loc[data['SMA50'] > data['SMA200'], 'Position'] = 1
data.loc[data['SMA50'] < data['SMA200'], 'Position'] = -1

# Ritorni
data['Returns'] = data['Close'].pct_change()
data['Strategy'] = data['Returns'] * data['Position'].shift(1)

# Grafico performance
data[['Returns', 'Strategy']].cumsum().plot(figsize=(10, 5))
plt.title('Strategia Media Mobile EUR/USD')
plt.grid()
plt.show()
