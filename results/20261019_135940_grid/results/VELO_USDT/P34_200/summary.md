# EMA Hourly Continuation — VELO/USDT P34_200

**Symbol:** VELO/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 406 |
| net_profit_factor | 0.7837 |
| net_win_rate | 0.5099 |
| gross_profit_factor | 1.0206 |
| gross_win_rate | 0.5099 |
| sharpe_ratio | -1.4841 |
| sortino_ratio | -0.4228 |
| max_drawdown | 0.4870 |
| cagr | -0.1829 |
| net_avg_win | 69.6413 |
| net_avg_loss | -92.4361 |
| avg_hold_time_bars | 26.5148 |
| exposure | 0.4893 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
