# EMA Hourly Continuation — MTL/USDT P34_55

**Symbol:** MTL/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 811 |
| net_profit_factor | 0.3718 |
| net_win_rate | 0.4020 |
| gross_profit_factor | 0.7913 |
| gross_win_rate | 0.4340 |
| sharpe_ratio | -8.9424 |
| sortino_ratio | -3.6229 |
| max_drawdown | 0.9898 |
| cagr | -0.8350 |
| net_avg_win | 17.9599 |
| net_avg_loss | -32.4715 |
| avg_hold_time_bars | 5.4451 |
| exposure | 0.1998 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
