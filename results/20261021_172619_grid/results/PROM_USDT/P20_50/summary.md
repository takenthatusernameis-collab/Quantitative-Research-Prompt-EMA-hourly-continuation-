# EMA Hourly Continuation — PROM/USDT P20_50

**Symbol:** PROM/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 563 |
| net_profit_factor | 0.5544 |
| net_win_rate | 0.4316 |
| gross_profit_factor | 0.7961 |
| gross_win_rate | 0.4352 |
| sharpe_ratio | -4.5597 |
| sortino_ratio | -1.5361 |
| max_drawdown | 0.8336 |
| cagr | -0.5104 |
| net_avg_win | 42.6858 |
| net_avg_loss | -58.4661 |
| avg_hold_time_bars | 7.8952 |
| exposure | 0.2020 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
