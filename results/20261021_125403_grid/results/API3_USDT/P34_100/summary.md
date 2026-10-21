# EMA Hourly Continuation — API3/USDT P34_100

**Symbol:** API3/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 451 |
| net_profit_factor | 0.8375 |
| net_win_rate | 0.5144 |
| gross_profit_factor | 1.0560 |
| gross_win_rate | 0.5144 |
| sharpe_ratio | -1.1870 |
| sortino_ratio | -0.3623 |
| max_drawdown | 0.4247 |
| cagr | -0.1550 |
| net_avg_win | 76.5726 |
| net_avg_loss | -96.8622 |
| avg_hold_time_bars | 13.7517 |
| exposure | 0.2819 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
