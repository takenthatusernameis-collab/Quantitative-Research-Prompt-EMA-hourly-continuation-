# EMA Hourly Continuation — KAS/USDT P12_20

**Symbol:** KAS/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1574 |
| net_profit_factor | 0.2549 |
| net_win_rate | 0.4047 |
| gross_profit_factor | 0.7491 |
| gross_win_rate | 0.4454 |
| sharpe_ratio | -14.1214 |
| sortino_ratio | -7.9954 |
| max_drawdown | 1.0000 |
| cagr | -0.9851 |
| net_avg_win | 5.3713 |
| net_avg_loss | -14.3236 |
| avg_hold_time_bars | 2.0591 |
| exposure | 0.1473 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
