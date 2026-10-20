# EMA Hourly Continuation — TNSR/USDT P34_200

**Symbol:** TNSR/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 413 |
| net_profit_factor | 0.6992 |
| net_win_rate | 0.4770 |
| gross_profit_factor | 0.9559 |
| gross_win_rate | 0.4867 |
| sharpe_ratio | -2.4315 |
| sortino_ratio | -0.6921 |
| max_drawdown | 0.5897 |
| cagr | -0.2817 |
| net_avg_win | 66.7824 |
| net_avg_loss | -87.1095 |
| avg_hold_time_bars | 27.0799 |
| exposure | 0.5061 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
