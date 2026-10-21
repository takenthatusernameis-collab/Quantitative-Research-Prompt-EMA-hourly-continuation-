# EMA Hourly Continuation — IOTA/USDT P8_89

**Symbol:** IOTA/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 537 |
| net_profit_factor | 0.8250 |
| net_win_rate | 0.5047 |
| gross_profit_factor | 1.0164 |
| gross_win_rate | 0.5047 |
| sharpe_ratio | -1.3876 |
| sortino_ratio | -0.4607 |
| max_drawdown | 0.4636 |
| cagr | -0.1936 |
| net_avg_win | 72.6154 |
| net_avg_loss | -89.6717 |
| avg_hold_time_bars | 26.0689 |
| exposure | 0.6363 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
