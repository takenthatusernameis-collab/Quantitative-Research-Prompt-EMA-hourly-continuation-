# EMA Hourly Continuation — BICO/USDT P20_34

**Symbol:** BICO/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 509 |
| net_profit_factor | 0.6504 |
| net_win_rate | 0.4794 |
| gross_profit_factor | 0.9247 |
| gross_win_rate | 0.4794 |
| sharpe_ratio | -3.0716 |
| sortino_ratio | -0.9917 |
| max_drawdown | 0.6818 |
| cagr | -0.3639 |
| net_avg_win | 51.7783 |
| net_avg_loss | -73.2976 |
| avg_hold_time_bars | 5.1768 |
| exposure | 0.1198 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
