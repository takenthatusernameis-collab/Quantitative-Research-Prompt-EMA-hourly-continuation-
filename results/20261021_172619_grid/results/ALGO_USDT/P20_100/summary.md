# EMA Hourly Continuation — ALGO/USDT P20_100

**Symbol:** ALGO/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 459 |
| net_profit_factor | 0.8477 |
| net_win_rate | 0.5163 |
| gross_profit_factor | 1.0576 |
| gross_win_rate | 0.5163 |
| sharpe_ratio | -1.0798 |
| sortino_ratio | -0.3325 |
| max_drawdown | 0.3571 |
| cagr | -0.1439 |
| net_avg_win | 75.8435 |
| net_avg_loss | -95.5177 |
| avg_hold_time_bars | 18.3094 |
| exposure | 0.3820 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
