# EMA Hourly Continuation — MAGIC/USDT P34_50

**Symbol:** MAGIC/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 400 |
| net_profit_factor | 0.7056 |
| net_win_rate | 0.5025 |
| gross_profit_factor | 1.0415 |
| gross_win_rate | 0.5025 |
| sharpe_ratio | -2.4165 |
| sortino_ratio | -0.6938 |
| max_drawdown | 0.5727 |
| cagr | -0.2723 |
| net_avg_win | 65.5801 |
| net_avg_loss | -93.8727 |
| avg_hold_time_bars | 5.2300 |
| exposure | 0.0951 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
