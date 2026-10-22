# EMA Hourly Continuation — ENA/USDT P8_100

**Symbol:** ENA/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 650 |
| net_profit_factor | 0.7483 |
| net_win_rate | 0.4954 |
| gross_profit_factor | 0.9805 |
| gross_win_rate | 0.4985 |
| sharpe_ratio | -2.3435 |
| sortino_ratio | -0.8341 |
| max_drawdown | 0.6622 |
| cagr | -0.3327 |
| net_avg_win | 58.9092 |
| net_avg_loss | -77.2801 |
| avg_hold_time_bars | 21.6200 |
| exposure | 0.6388 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
