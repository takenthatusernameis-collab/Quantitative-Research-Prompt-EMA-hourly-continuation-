# EMA Hourly Continuation — AEVO/USDT P89_200

**Symbol:** AEVO/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 389 |
| net_profit_factor | 0.6842 |
| net_win_rate | 0.4936 |
| gross_profit_factor | 0.9804 |
| gross_win_rate | 0.4987 |
| sharpe_ratio | -2.2541 |
| sortino_ratio | -0.6310 |
| max_drawdown | 0.5451 |
| cagr | -0.2540 |
| net_avg_win | 58.9487 |
| net_avg_loss | -83.9728 |
| avg_hold_time_bars | 13.2956 |
| exposure | 0.2340 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
