# EMA Hourly Continuation — ORDI/USDT P50_200

**Symbol:** ORDI/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 309 |
| net_profit_factor | 0.7787 |
| net_win_rate | 0.4822 |
| gross_profit_factor | 0.9290 |
| gross_win_rate | 0.4822 |
| sharpe_ratio | -1.3516 |
| sortino_ratio | -0.3386 |
| max_drawdown | 0.3652 |
| cagr | -0.1447 |
| net_avg_win | 76.6524 |
| net_avg_loss | -91.6741 |
| avg_hold_time_bars | 26.4498 |
| exposure | 0.3715 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
