# EMA Hourly Continuation — NEAR/USDT P20_100

**Symbol:** NEAR/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 642 |
| net_profit_factor | 0.6536 |
| net_win_rate | 0.4704 |
| gross_profit_factor | 0.9344 |
| gross_win_rate | 0.4751 |
| sharpe_ratio | -3.7597 |
| sortino_ratio | -1.3428 |
| max_drawdown | 0.8072 |
| cagr | -0.4719 |
| net_avg_win | 49.9073 |
| net_avg_loss | -67.8235 |
| avg_hold_time_bars | 13.9766 |
| exposure | 0.4079 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
