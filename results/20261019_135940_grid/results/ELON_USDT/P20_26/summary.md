# EMA Hourly Continuation — ELON/USDT P20_26

**Symbol:** ELON/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1041 |
| net_profit_factor | 0.1990 |
| net_win_rate | 0.3593 |
| gross_profit_factor | 0.5864 |
| gross_win_rate | 0.3881 |
| sharpe_ratio | -13.2484 |
| sortino_ratio | -6.2637 |
| max_drawdown | 0.9997 |
| cagr | -0.9602 |
| net_avg_win | 6.6405 |
| net_avg_loss | -18.7114 |
| avg_hold_time_bars | 2.2815 |
| exposure | 0.1080 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
