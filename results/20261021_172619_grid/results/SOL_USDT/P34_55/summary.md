# EMA Hourly Continuation — SOL/USDT P34_55

**Symbol:** SOL/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 269 |
| net_profit_factor | 0.8392 |
| net_win_rate | 0.5539 |
| gross_profit_factor | 1.2442 |
| gross_win_rate | 0.5539 |
| sharpe_ratio | -0.9104 |
| sortino_ratio | -0.2168 |
| max_drawdown | 0.2764 |
| cagr | -0.0953 |
| net_avg_win | 77.8993 |
| net_avg_loss | -115.2546 |
| avg_hold_time_bars | 5.8178 |
| exposure | 0.0711 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
