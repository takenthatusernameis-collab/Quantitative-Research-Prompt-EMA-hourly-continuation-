# EMA Hourly Continuation — IMX/USDT P34_55

**Symbol:** IMX/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 890 |
| net_profit_factor | 0.5390 |
| net_win_rate | 0.4888 |
| gross_profit_factor | 1.0060 |
| gross_win_rate | 0.5090 |
| sharpe_ratio | -5.8622 |
| sortino_ratio | -2.4536 |
| max_drawdown | 0.9559 |
| cagr | -0.7036 |
| net_avg_win | 25.6298 |
| net_avg_loss | -45.4587 |
| avg_hold_time_bars | 2.9966 |
| exposure | 0.1207 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
