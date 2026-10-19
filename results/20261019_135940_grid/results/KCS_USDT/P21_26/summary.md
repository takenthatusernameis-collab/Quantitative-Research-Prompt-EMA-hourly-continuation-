# EMA Hourly Continuation — KCS/USDT P21_26

**Symbol:** KCS/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1161 |
| net_profit_factor | 0.0366 |
| net_win_rate | 0.1697 |
| gross_profit_factor | 0.4207 |
| gross_win_rate | 0.3170 |
| sharpe_ratio | -22.3259 |
| sortino_ratio | -13.0649 |
| max_drawdown | 1.0000 |
| cagr | -0.9993 |
| net_avg_win | 1.9266 |
| net_avg_loss | -10.7672 |
| avg_hold_time_bars | 2.0568 |
| exposure | 0.1085 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
