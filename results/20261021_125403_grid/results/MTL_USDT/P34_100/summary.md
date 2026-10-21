# EMA Hourly Continuation — MTL/USDT P34_100

**Symbol:** MTL/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 449 |
| net_profit_factor | 0.5740 |
| net_win_rate | 0.4365 |
| gross_profit_factor | 0.7898 |
| gross_win_rate | 0.4365 |
| sharpe_ratio | -3.9084 |
| sortino_ratio | -1.1736 |
| max_drawdown | 0.7479 |
| cagr | -0.4193 |
| net_avg_win | 51.3061 |
| net_avg_loss | -69.2400 |
| avg_hold_time_bars | 17.2806 |
| exposure | 0.3511 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
