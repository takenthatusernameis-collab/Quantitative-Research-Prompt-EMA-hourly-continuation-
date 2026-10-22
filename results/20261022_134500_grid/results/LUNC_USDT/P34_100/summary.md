# EMA Hourly Continuation — LUNC/USDT P34_100

**Symbol:** LUNC/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 693 |
| net_profit_factor | 0.5041 |
| net_win_rate | 0.4675 |
| gross_profit_factor | 0.9203 |
| gross_win_rate | 0.4848 |
| sharpe_ratio | -5.3074 |
| sortino_ratio | -1.9755 |
| max_drawdown | 0.9139 |
| cagr | -0.6116 |
| net_avg_win | 28.4577 |
| net_avg_loss | -49.5668 |
| avg_hold_time_bars | 8.8110 |
| exposure | 0.2775 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
