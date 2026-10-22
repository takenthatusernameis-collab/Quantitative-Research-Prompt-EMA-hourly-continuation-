# EMA Hourly Continuation — SWFTC/USDT P21_200

**Symbol:** SWFTC/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 357 |
| net_profit_factor | 0.7342 |
| net_win_rate | 0.4678 |
| gross_profit_factor | 0.8895 |
| gross_win_rate | 0.4678 |
| sharpe_ratio | -1.9693 |
| sortino_ratio | -0.5281 |
| max_drawdown | 0.4660 |
| cagr | -0.2163 |
| net_avg_win | 75.7314 |
| net_avg_loss | -90.6582 |
| avg_hold_time_bars | 31.9048 |
| exposure | 0.5177 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
