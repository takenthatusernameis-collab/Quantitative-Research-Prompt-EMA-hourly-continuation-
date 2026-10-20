# EMA Hourly Continuation — LQTY/USDT P26_100

**Symbol:** LQTY/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 655 |
| net_profit_factor | 0.6169 |
| net_win_rate | 0.4626 |
| gross_profit_factor | 0.8971 |
| gross_win_rate | 0.4687 |
| sharpe_ratio | -4.0384 |
| sortino_ratio | -1.4651 |
| max_drawdown | 0.8302 |
| cagr | -0.4933 |
| net_avg_win | 43.5740 |
| net_avg_loss | -60.8050 |
| avg_hold_time_bars | 12.3710 |
| exposure | 0.3667 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
