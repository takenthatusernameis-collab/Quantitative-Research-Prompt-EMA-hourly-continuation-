# EMA Hourly Continuation — APE/USDT P8_50

**Symbol:** APE/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1139 |
| net_profit_factor | 0.5927 |
| net_win_rate | 0.4486 |
| gross_profit_factor | 0.9460 |
| gross_win_rate | 0.4592 |
| sharpe_ratio | -6.8114 |
| sortino_ratio | -3.2451 |
| max_drawdown | 0.9802 |
| cagr | -0.7859 |
| net_avg_win | 27.8890 |
| net_avg_loss | -38.2848 |
| avg_hold_time_bars | 8.7480 |
| exposure | 0.4529 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
