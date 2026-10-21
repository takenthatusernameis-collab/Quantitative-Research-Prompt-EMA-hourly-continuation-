# EMA Hourly Continuation — ORDI/USDT P21_89

**Symbol:** ORDI/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 490 |
| net_profit_factor | 0.6909 |
| net_win_rate | 0.4571 |
| gross_profit_factor | 0.8455 |
| gross_win_rate | 0.4571 |
| sharpe_ratio | -2.6516 |
| sortino_ratio | -0.8334 |
| max_drawdown | 0.6355 |
| cagr | -0.3181 |
| net_avg_win | 61.6258 |
| net_avg_loss | -75.1156 |
| avg_hold_time_bars | 14.1408 |
| exposure | 0.3150 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
