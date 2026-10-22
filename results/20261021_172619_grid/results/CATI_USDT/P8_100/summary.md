# EMA Hourly Continuation — CATI/USDT P8_100

**Symbol:** CATI/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 300 |
| net_profit_factor | 0.7559 |
| net_win_rate | 0.4800 |
| gross_profit_factor | 0.9261 |
| gross_win_rate | 0.4800 |
| sharpe_ratio | -1.7639 |
| sortino_ratio | -0.4770 |
| max_drawdown | 0.4643 |
| cagr | -0.1992 |
| net_avg_win | 79.6310 |
| net_avg_loss | -97.2431 |
| avg_hold_time_bars | 41.9900 |
| exposure | 0.6905 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
