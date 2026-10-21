# EMA Hourly Continuation — ORDI/USDT P8_100

**Symbol:** ORDI/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 482 |
| net_profit_factor | 0.7432 |
| net_win_rate | 0.4606 |
| gross_profit_factor | 0.8812 |
| gross_win_rate | 0.4606 |
| sharpe_ratio | -2.3126 |
| sortino_ratio | -0.7204 |
| max_drawdown | 0.6085 |
| cagr | -0.2823 |
| net_avg_win | 73.6735 |
| net_avg_loss | -84.6443 |
| avg_hold_time_bars | 29.2822 |
| exposure | 0.6415 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
