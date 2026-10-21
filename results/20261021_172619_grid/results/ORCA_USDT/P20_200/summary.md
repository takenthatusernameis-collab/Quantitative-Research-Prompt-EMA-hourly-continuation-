# EMA Hourly Continuation — ORCA/USDT P20_200

**Symbol:** ORCA/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 325 |
| net_profit_factor | 0.7962 |
| net_win_rate | 0.5015 |
| gross_profit_factor | 0.9787 |
| gross_win_rate | 0.5015 |
| sharpe_ratio | -1.2164 |
| sortino_ratio | -0.3124 |
| max_drawdown | 0.3766 |
| cagr | -0.1362 |
| net_avg_win | 73.7276 |
| net_avg_loss | -93.1713 |
| avg_hold_time_bars | 43.6708 |
| exposure | 0.6451 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
