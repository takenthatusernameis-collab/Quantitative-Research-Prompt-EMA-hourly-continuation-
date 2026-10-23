# EMA Hourly Continuation — ANKR/USDT P12_20

**Symbol:** ANKR/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1477 |
| net_profit_factor | 0.2768 |
| net_win_rate | 0.3778 |
| gross_profit_factor | 0.7464 |
| gross_win_rate | 0.4232 |
| sharpe_ratio | -14.9992 |
| sortino_ratio | -8.3023 |
| max_drawdown | 1.0000 |
| cagr | -0.9867 |
| net_avg_win | 6.8582 |
| net_avg_loss | -15.0453 |
| avg_hold_time_bars | 2.7739 |
| exposure | 0.1862 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
