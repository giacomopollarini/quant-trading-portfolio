# Strategia Breakout su EUR/USD

## Descrizione
Questa strategia entra long quando il prezzo rompe il massimo a 20 giorni, ed entra short quando rompe il minimo. È pensata per mercati in trend.

## Logica operativa
- Long se Close > High_20 (massimo delle ultime 20 candele)
- Short se Close < Low_20
- Exit a cambio segnale o stop dinamico

## Dati utilizzati
- EURUSD=X (Yahoo Finance)
- Timeframe: Daily

## Performance
Include rendimento cumulato della strategia rispetto al buy & hold

## Come eseguire
Script Python o notebook incluso nella cartella.
