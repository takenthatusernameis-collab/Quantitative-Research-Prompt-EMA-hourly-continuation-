# EMA Hourly Continuation — DEEP/USDT P20_200

**Symbol:** DEEP/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 211 |
| net_profit_factor | 0.8796 |
| net_win_rate | 0.5024 |
| gross_profit_factor | 0.9926 |
| gross_win_rate | 0.5024 |
| sharpe_ratio | -0.6026 |
| sortino_ratio | -0.1396 |
| max_drawdown | 0.1447 |
| cagr | -0.0646 |
| net_avg_win | 86.8305 |
| net_avg_loss | -99.6603 |
| avg_hold_time_bars | 56.5166 |
| exposure | 0.6752 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
