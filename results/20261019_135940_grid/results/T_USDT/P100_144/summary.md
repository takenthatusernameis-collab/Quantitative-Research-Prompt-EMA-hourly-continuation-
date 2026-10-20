# EMA Hourly Continuation — T/USDT P100_144

**Symbol:** T/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 469 |
| net_profit_factor | 0.4154 |
| net_win_rate | 0.4371 |
| gross_profit_factor | 0.8410 |
| gross_win_rate | 0.4712 |
| sharpe_ratio | -5.5729 |
| sortino_ratio | -1.7016 |
| max_drawdown | 0.8835 |
| cagr | -0.5708 |
| net_avg_win | 30.5540 |
| net_avg_loss | -57.1197 |
| avg_hold_time_bars | 5.9019 |
| exposure | 0.1253 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
