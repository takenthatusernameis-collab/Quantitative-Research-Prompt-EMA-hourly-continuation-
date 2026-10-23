# EMA Hourly Continuation — CARV/USDT P8_26

**Symbol:** CARV/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1068 |
| net_profit_factor | 0.5811 |
| net_win_rate | 0.4747 |
| gross_profit_factor | 1.0585 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -7.5532 |
| sortino_ratio | -3.8519 |
| max_drawdown | 0.9796 |
| cagr | -0.8508 |
| net_avg_win | 26.7821 |
| net_avg_loss | -41.6535 |
| avg_hold_time_bars | 5.4466 |
| exposure | 0.3273 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
