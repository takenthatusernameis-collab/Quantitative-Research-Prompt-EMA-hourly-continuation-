# EMA Hourly Continuation — CFX/USDT P12_26

**Symbol:** CFX/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1418 |
| net_profit_factor | 0.3474 |
| net_win_rate | 0.3815 |
| gross_profit_factor | 0.7839 |
| gross_win_rate | 0.4048 |
| sharpe_ratio | -13.2486 |
| sortino_ratio | -7.0977 |
| max_drawdown | 0.9999 |
| cagr | -0.9737 |
| net_avg_win | 9.8374 |
| net_avg_loss | -17.4697 |
| avg_hold_time_bars | 2.9274 |
| exposure | 0.1887 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
