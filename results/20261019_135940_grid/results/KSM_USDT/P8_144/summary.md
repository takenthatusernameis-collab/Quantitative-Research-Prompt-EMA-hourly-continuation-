# EMA Hourly Continuation — KSM/USDT P8_144

**Symbol:** KSM/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 458 |
| net_profit_factor | 0.6513 |
| net_win_rate | 0.4651 |
| gross_profit_factor | 0.9352 |
| gross_win_rate | 0.4760 |
| sharpe_ratio | -3.2447 |
| sortino_ratio | -0.9773 |
| max_drawdown | 0.6942 |
| cagr | -0.3703 |
| net_avg_win | 60.2413 |
| net_avg_loss | -80.4157 |
| avg_hold_time_bars | 36.4803 |
| exposure | 0.7595 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
