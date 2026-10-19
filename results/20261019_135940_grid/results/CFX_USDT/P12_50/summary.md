# EMA Hourly Continuation — CFX/USDT P12_50

**Symbol:** CFX/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1051 |
| net_profit_factor | 0.5303 |
| net_win_rate | 0.4405 |
| gross_profit_factor | 0.8789 |
| gross_win_rate | 0.4510 |
| sharpe_ratio | -7.4091 |
| sortino_ratio | -3.3769 |
| max_drawdown | 0.9844 |
| cagr | -0.8062 |
| net_avg_win | 23.9941 |
| net_avg_loss | -35.6242 |
| avg_hold_time_bars | 7.4301 |
| exposure | 0.3550 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
