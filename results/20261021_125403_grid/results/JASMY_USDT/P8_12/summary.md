# EMA Hourly Continuation — JASMY/USDT P8_12

**Symbol:** JASMY/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 195 |
| net_profit_factor | 0.7234 |
| net_win_rate | 0.4974 |
| gross_profit_factor | 0.9765 |
| gross_win_rate | 0.4974 |
| sharpe_ratio | -1.3764 |
| sortino_ratio | -0.2758 |
| max_drawdown | 0.3166 |
| cagr | -0.1188 |
| net_avg_win | 73.3751 |
| net_avg_loss | -100.3911 |
| avg_hold_time_bars | 4.7436 |
| exposure | 0.0420 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
