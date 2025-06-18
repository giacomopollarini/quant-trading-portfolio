# Strategia Media Mobile
# Moving Average Crossover Strategy – EUR/USD

## 🔍 Description

This is a basic moving average crossover strategy built in Python to test trend-following logic on the EUR/USD pair.

The strategy enters a **long position** when the 50-day simple moving average (SMA) crosses above the 200-day SMA.  
It goes **short** when the 50-day SMA crosses below the 200-day SMA.

It is implemented as part of my transition from discretionary trading to systematic strategy development.

---

## 🧠 Strategy Logic

- **Buy signal**: SMA(50) > SMA(200)
- **Sell signal**: SMA(50) < SMA(200)
- Position is held as long as the condition remains true
- Daily close prices used for signal generation

---

## 🧪 Backtest Parameters

- **Asset**: EUR/USD (`EURUSD=X` via Yahoo Finance)
- **Period**: 2020-01-01 to 2023-01-01
- **Libraries**: `pandas`, `matplotlib`, `yfinance`

---

## 📈 Output

The script generates a cumulative return chart comparing:
- Strategy performance
- Buy & hold baseline

---

## ⚠️ Notes

This is a simple educational strategy used to test:
- Moving average logic
- Data handling with pandas
- Backtesting logic using position-based returns

The goal is to learn and build more robust systems over time.

---

## 📂 Files

- `moving_average_strategy.py`: Full strategy code
- `README.md`: This file



