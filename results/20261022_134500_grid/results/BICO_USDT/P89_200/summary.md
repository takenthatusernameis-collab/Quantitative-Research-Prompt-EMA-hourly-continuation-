# EMA Hourly Continuation — BICO/USDT P89_200

**Symbol:** BICO/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 374 |
| net_profit_factor | 0.6564 |
| net_win_rate | 0.4599 |
| gross_profit_factor | 0.9157 |
| gross_win_rate | 0.4706 |
| sharpe_ratio | -2.7296 |
| sortino_ratio | -0.7478 |
| max_drawdown | 0.5981 |
| cagr | -0.2940 |
| net_avg_win | 64.7389 |
| net_avg_loss | -83.9808 |
| avg_hold_time_bars | 13.4545 |
| exposure | 0.2287 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
