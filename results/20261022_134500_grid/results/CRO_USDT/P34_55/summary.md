# EMA Hourly Continuation — CRO/USDT P34_55

**Symbol:** CRO/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 881 |
| net_profit_factor | 0.2753 |
| net_win_rate | 0.3973 |
| gross_profit_factor | 0.7950 |
| gross_win_rate | 0.4529 |
| sharpe_ratio | -10.5208 |
| sortino_ratio | -4.4636 |
| max_drawdown | 0.9973 |
| cagr | -0.9046 |
| net_avg_win | 10.8236 |
| net_avg_loss | -25.9150 |
| avg_hold_time_bars | 3.3031 |
| exposure | 0.1323 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
