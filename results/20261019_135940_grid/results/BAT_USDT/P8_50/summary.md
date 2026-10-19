# EMA Hourly Continuation — BAT/USDT P8_50

**Symbol:** BAT/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1086 |
| net_profit_factor | 0.5098 |
| net_win_rate | 0.4678 |
| gross_profit_factor | 0.9217 |
| gross_win_rate | 0.4862 |
| sharpe_ratio | -6.1532 |
| sortino_ratio | -2.8484 |
| max_drawdown | 0.9708 |
| cagr | -0.7484 |
| net_avg_win | 19.8336 |
| net_avg_loss | -34.1916 |
| avg_hold_time_bars | 9.2210 |
| exposure | 0.4552 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
