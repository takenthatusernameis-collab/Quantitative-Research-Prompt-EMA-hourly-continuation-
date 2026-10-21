# EMA Hourly Continuation — PROM/USDT P20_89

**Symbol:** PROM/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 504 |
| net_profit_factor | 0.5954 |
| net_win_rate | 0.4385 |
| gross_profit_factor | 0.8013 |
| gross_win_rate | 0.4405 |
| sharpe_ratio | -3.7273 |
| sortino_ratio | -1.1850 |
| max_drawdown | 0.7514 |
| cagr | -0.4222 |
| net_avg_win | 49.8042 |
| net_avg_loss | -65.3187 |
| avg_hold_time_bars | 15.9087 |
| exposure | 0.3645 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
