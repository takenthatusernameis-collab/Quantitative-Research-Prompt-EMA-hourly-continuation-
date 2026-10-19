# EMA Hourly Continuation — DOGE/USDT P144_200

**Symbol:** DOGE/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 414 |
| net_profit_factor | 0.4895 |
| net_win_rate | 0.4662 |
| gross_profit_factor | 1.0210 |
| gross_win_rate | 0.4976 |
| sharpe_ratio | -5.1059 |
| sortino_ratio | -1.4539 |
| max_drawdown | 0.8476 |
| cagr | -0.5220 |
| net_avg_win | 41.9020 |
| net_avg_loss | -74.7541 |
| avg_hold_time_bars | 4.2754 |
| exposure | 0.0805 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
