# EMA Hourly Continuation — ENA/USDT P8_89

**Symbol:** ENA/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 744 |
| net_profit_factor | 0.7582 |
| net_win_rate | 0.4973 |
| gross_profit_factor | 0.9846 |
| gross_win_rate | 0.4987 |
| sharpe_ratio | -2.4051 |
| sortino_ratio | -0.9273 |
| max_drawdown | 0.6912 |
| cagr | -0.3543 |
| net_avg_win | 56.4957 |
| net_avg_loss | -73.7140 |
| avg_hold_time_bars | 17.8884 |
| exposure | 0.6050 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
