# EMA Hourly Continuation — CARV/USDT P20_89

**Symbol:** CARV/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 528 |
| net_profit_factor | 0.6329 |
| net_win_rate | 0.4697 |
| gross_profit_factor | 0.9694 |
| gross_win_rate | 0.4848 |
| sharpe_ratio | -3.9268 |
| sortino_ratio | -1.4037 |
| max_drawdown | 0.7639 |
| cagr | -0.4919 |
| net_avg_win | 51.9174 |
| net_avg_loss | -72.6534 |
| avg_hold_time_bars | 13.3598 |
| exposure | 0.3970 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
