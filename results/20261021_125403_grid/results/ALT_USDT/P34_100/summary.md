# EMA Hourly Continuation — ALT/USDT P34_100

**Symbol:** ALT/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 450 |
| net_profit_factor | 0.7699 |
| net_win_rate | 0.4956 |
| gross_profit_factor | 0.9648 |
| gross_win_rate | 0.4956 |
| sharpe_ratio | -1.6652 |
| sortino_ratio | -0.5053 |
| max_drawdown | 0.4583 |
| cagr | -0.2084 |
| net_avg_win | 66.5864 |
| net_avg_loss | -84.9671 |
| avg_hold_time_bars | 14.5844 |
| exposure | 0.2983 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
