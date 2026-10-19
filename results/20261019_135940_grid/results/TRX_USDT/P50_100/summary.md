# EMA Hourly Continuation — TRX/USDT P50_100

**Symbol:** TRX/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 538 |
| net_profit_factor | 0.2743 |
| net_win_rate | 0.3717 |
| gross_profit_factor | 1.0883 |
| gross_win_rate | 0.5093 |
| sharpe_ratio | -9.3400 |
| sortino_ratio | -3.2031 |
| max_drawdown | 0.9850 |
| cagr | -0.8121 |
| net_avg_win | 18.6196 |
| net_avg_loss | -40.1592 |
| avg_hold_time_bars | 6.4833 |
| exposure | 0.1585 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
