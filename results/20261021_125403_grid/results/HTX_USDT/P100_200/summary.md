# EMA Hourly Continuation — HTX/USDT P100_200

**Symbol:** HTX/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 262 |
| net_profit_factor | 0.4583 |
| net_win_rate | 0.4160 |
| gross_profit_factor | 0.7862 |
| gross_win_rate | 0.4160 |
| sharpe_ratio | -4.3996 |
| sortino_ratio | -1.0286 |
| max_drawdown | 0.7050 |
| cagr | -0.3798 |
| net_avg_win | 54.3614 |
| net_avg_loss | -84.5040 |
| avg_hold_time_bars | 14.9771 |
| exposure | 0.1776 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
