# EMA Hourly Continuation — ORDI/USDT P8_100

**Symbol:** ORDI/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 703 |
| net_profit_factor | 0.6254 |
| net_win_rate | 0.4538 |
| gross_profit_factor | 0.8783 |
| gross_win_rate | 0.4552 |
| sharpe_ratio | -4.5544 |
| sortino_ratio | -1.6947 |
| max_drawdown | 0.8753 |
| cagr | -0.5566 |
| net_avg_win | 45.5408 |
| net_avg_loss | -60.4952 |
| avg_hold_time_bars | 20.5704 |
| exposure | 0.6573 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
