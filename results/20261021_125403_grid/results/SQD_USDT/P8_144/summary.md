# EMA Hourly Continuation — SQD/USDT P8_144

**Symbol:** SQD/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 448 |
| net_profit_factor | 0.8180 |
| net_win_rate | 0.4844 |
| gross_profit_factor | 0.9251 |
| gross_win_rate | 0.4844 |
| sharpe_ratio | -1.2541 |
| sortino_ratio | -0.3847 |
| max_drawdown | 0.3809 |
| cagr | -0.1647 |
| net_avg_win | 73.3336 |
| net_avg_loss | -84.2188 |
| avg_hold_time_bars | 30.6228 |
| exposure | 0.6448 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
