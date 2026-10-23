# EMA Hourly Continuation — SQD/USDT P8_20

**Symbol:** SQD/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1509 |
| net_profit_factor | 0.5111 |
| net_win_rate | 0.4228 |
| gross_profit_factor | 0.9173 |
| gross_win_rate | 0.4407 |
| sharpe_ratio | -10.6048 |
| sortino_ratio | -5.8616 |
| max_drawdown | 0.9993 |
| cagr | -0.9477 |
| net_avg_win | 16.3717 |
| net_avg_loss | -23.4643 |
| avg_hold_time_bars | 2.8337 |
| exposure | 0.2010 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
