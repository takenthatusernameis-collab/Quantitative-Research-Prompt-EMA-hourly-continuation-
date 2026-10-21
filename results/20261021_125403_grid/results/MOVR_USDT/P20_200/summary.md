# EMA Hourly Continuation — MOVR/USDT P20_200

**Symbol:** MOVR/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 348 |
| net_profit_factor | 0.7580 |
| net_win_rate | 0.4770 |
| gross_profit_factor | 0.8996 |
| gross_win_rate | 0.4770 |
| sharpe_ratio | -1.5175 |
| sortino_ratio | -0.4028 |
| max_drawdown | 0.4357 |
| cagr | -0.1704 |
| net_avg_win | 70.6588 |
| net_avg_loss | -85.0201 |
| avg_hold_time_bars | 40.5201 |
| exposure | 0.6410 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
