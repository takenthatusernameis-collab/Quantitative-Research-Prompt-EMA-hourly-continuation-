# EMA Hourly Continuation — CRO/USDT P8_144

**Symbol:** CRO/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 438 |
| net_profit_factor | 0.5451 |
| net_win_rate | 0.4680 |
| gross_profit_factor | 0.9014 |
| gross_win_rate | 0.4749 |
| sharpe_ratio | -3.7523 |
| sortino_ratio | -1.1039 |
| max_drawdown | 0.7502 |
| cagr | -0.4165 |
| net_avg_win | 43.3415 |
| net_avg_loss | -69.9549 |
| avg_hold_time_bars | 39.0890 |
| exposure | 0.7782 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
