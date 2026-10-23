# EMA Hourly Continuation — MASK/USDT P12_21

**Symbol:** MASK/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1470 |
| net_profit_factor | 0.2284 |
| net_win_rate | 0.4041 |
| gross_profit_factor | 0.7103 |
| gross_win_rate | 0.4517 |
| sharpe_ratio | -13.7399 |
| sortino_ratio | -7.5046 |
| max_drawdown | 1.0000 |
| cagr | -0.9807 |
| net_avg_win | 4.9840 |
| net_avg_loss | -14.7945 |
| avg_hold_time_bars | 2.7918 |
| exposure | 0.1865 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
