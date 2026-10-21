# EMA Hourly Continuation — KSM/USDT P21_55

**Symbol:** KSM/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 548 |
| net_profit_factor | 0.6846 |
| net_win_rate | 0.4854 |
| gross_profit_factor | 0.9388 |
| gross_win_rate | 0.4854 |
| sharpe_ratio | -2.8250 |
| sortino_ratio | -0.9464 |
| max_drawdown | 0.6701 |
| cagr | -0.3510 |
| net_avg_win | 54.0508 |
| net_avg_loss | -74.4730 |
| avg_hold_time_bars | 8.2993 |
| exposure | 0.2067 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
