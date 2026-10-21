# EMA Hourly Continuation — KSM/USDT P20_100

**Symbol:** KSM/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 454 |
| net_profit_factor | 0.7322 |
| net_win_rate | 0.4868 |
| gross_profit_factor | 0.9444 |
| gross_win_rate | 0.4868 |
| sharpe_ratio | -2.1403 |
| sortino_ratio | -0.6509 |
| max_drawdown | 0.5697 |
| cagr | -0.2590 |
| net_avg_win | 65.4447 |
| net_avg_loss | -84.7782 |
| avg_hold_time_bars | 21.6145 |
| exposure | 0.4460 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
