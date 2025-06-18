
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# Scarica i dati storici EUR/USD
data = yf.download('EURUSD=X', start='2020-01-01', end='2023-01-01')

# Calcolo del massimo e minimo a 20 giorni
data['20d_high'] = data['High'].rolling(window=20).max()
data['20d_low'] = data['Low'].rolling(window=20).min()

# Generazione segnali
data['Signal'] = 0
data.loc[data['Close'] > data['20d_high'], 'Signal'] = 1
data.loc[data['Close'] < data['20d_low'], 'Signal'] = -1

# Forward-fill delle posizioni
data['Position'] = data['Signal'].replace(to_replace=0, method='ffill')

# Calcolo ritorni
data['Returns'] = data['Close'].pct_change()
data['Strategy'] = data['Returns'] * data['Position'].shift(1)

# Grafico performance cumulative
(data[['Returns', 'Strategy']] + 1).cumprod().plot(figsize=(10, 5))
plt.title('Breakout Strategy vs Buy & Hold')
plt.grid(True)
plt.show()
