# EMA Hourly Continuation — THETA/USDT P12_26

**Symbol:** THETA/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 449 |
| net_profit_factor | 0.7429 |
| net_win_rate | 0.5056 |
| gross_profit_factor | 1.0149 |
| gross_win_rate | 0.5056 |
| sharpe_ratio | -1.9510 |
| sortino_ratio | -0.5945 |
| max_drawdown | 0.5193 |
| cagr | -0.2380 |
| net_avg_win | 62.9755 |
| net_avg_loss | -86.6794 |
| avg_hold_time_bars | 5.6414 |
| exposure | 0.1151 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
