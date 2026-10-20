# EMA Hourly Continuation — DEEP/USDT P20_55

**Symbol:** DEEP/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 690 |
| net_profit_factor | 0.6798 |
| net_win_rate | 0.4913 |
| gross_profit_factor | 1.0147 |
| gross_win_rate | 0.5014 |
| sharpe_ratio | -4.0030 |
| sortino_ratio | -1.6493 |
| max_drawdown | 0.8053 |
| cagr | -0.5479 |
| net_avg_win | 49.9823 |
| net_avg_loss | -71.0151 |
| avg_hold_time_bars | 6.0812 |
| exposure | 0.2376 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
