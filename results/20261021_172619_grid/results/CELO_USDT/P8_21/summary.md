# EMA Hourly Continuation — CELO/USDT P8_21

**Symbol:** CELO/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 678 |
| net_profit_factor | 0.6505 |
| net_win_rate | 0.4676 |
| gross_profit_factor | 0.9218 |
| gross_win_rate | 0.4676 |
| sharpe_ratio | -4.0022 |
| sortino_ratio | -1.4869 |
| max_drawdown | 0.8234 |
| cagr | -0.4948 |
| net_avg_win | 48.2331 |
| net_avg_loss | -65.1078 |
| avg_hold_time_bars | 5.4808 |
| exposure | 0.1682 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
