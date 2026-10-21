# EMA Hourly Continuation — KAS/USDT P100_144

**Symbol:** KAS/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 223 |
| net_profit_factor | 0.7288 |
| net_win_rate | 0.5067 |
| gross_profit_factor | 1.0008 |
| gross_win_rate | 0.5067 |
| sharpe_ratio | -1.3609 |
| sortino_ratio | -0.2920 |
| max_drawdown | 0.3102 |
| cagr | -0.1249 |
| net_avg_win | 67.7104 |
| net_avg_loss | -95.4412 |
| avg_hold_time_bars | 6.4484 |
| exposure | 0.0654 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
