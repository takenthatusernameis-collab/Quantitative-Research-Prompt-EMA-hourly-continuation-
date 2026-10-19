# EMA Hourly Continuation — ADA/USDT P34_100

**Symbol:** ADA/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 639 |
| net_profit_factor | 0.4896 |
| net_win_rate | 0.4444 |
| gross_profit_factor | 0.8147 |
| gross_win_rate | 0.4601 |
| sharpe_ratio | -5.3850 |
| sortino_ratio | -1.9093 |
| max_drawdown | 0.9074 |
| cagr | -0.6075 |
| net_avg_win | 30.5453 |
| net_avg_loss | -49.9153 |
| avg_hold_time_bars | 8.7637 |
| exposure | 0.2545 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
