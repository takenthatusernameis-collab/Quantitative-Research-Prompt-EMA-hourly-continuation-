# EMA Hourly Continuation — WEMIX/USDT P8_144

**Symbol:** WEMIX/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 752 |
| net_profit_factor | 0.3561 |
| net_win_rate | 0.3165 |
| gross_profit_factor | 0.5230 |
| gross_win_rate | 0.3218 |
| sharpe_ratio | -10.0158 |
| sortino_ratio | -3.8840 |
| max_drawdown | 0.9926 |
| cagr | -0.8559 |
| net_avg_win | 23.0542 |
| net_avg_loss | -29.9802 |
| avg_hold_time_bars | 21.9335 |
| exposure | 0.7497 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
