# EMA Hourly Continuation — CSPR/USDT P12_20

**Symbol:** CSPR/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 263 |
| net_profit_factor | 0.5465 |
| net_win_rate | 0.4030 |
| gross_profit_factor | 0.7249 |
| gross_win_rate | 0.4030 |
| sharpe_ratio | -3.3576 |
| sortino_ratio | -0.7714 |
| max_drawdown | 0.5918 |
| cagr | -0.3000 |
| net_avg_win | 67.2846 |
| net_avg_loss | -83.1193 |
| avg_hold_time_bars | 5.4905 |
| exposure | 0.0656 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
