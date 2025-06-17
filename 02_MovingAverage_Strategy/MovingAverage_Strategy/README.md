# Strategia Media Mobile su EUR/USD

## Descrizione
Strategia trend-following basata su crossover tra medie mobili semplici:
- SMA50 (media mobile a 50 giorni)
- SMA200 (media mobile a 200 giorni)

## Logica operativa
- Long se SMA50 > SMA200
- Short se SMA50 < SMA200
- Exit a cambio segnale

## Dati utilizzati
- EURUSD=X da Yahoo Finance
- Timeframe: Daily

## Output
Grafico con rendimento cumulato della strategia rispetto al buy & hold.

## Come usare
Esegui lo script `moving_average_strategy.py` con Python installato (richiede `pandas`, `matplotlib`, `yfinance`).
