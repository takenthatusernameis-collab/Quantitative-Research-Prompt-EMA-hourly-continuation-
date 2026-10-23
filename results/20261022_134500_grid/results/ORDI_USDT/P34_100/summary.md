# EMA Hourly Continuation — ORDI/USDT P34_100

**Symbol:** ORDI/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 656 |
| net_profit_factor | 0.5978 |
| net_win_rate | 0.4588 |
| gross_profit_factor | 0.8745 |
| gross_win_rate | 0.4665 |
| sharpe_ratio | -4.4013 |
| sortino_ratio | -1.5931 |
| max_drawdown | 0.8523 |
| cagr | -0.5282 |
| net_avg_win | 41.8972 |
| net_avg_loss | -59.4237 |
| avg_hold_time_bars | 9.4116 |
| exposure | 0.2806 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
