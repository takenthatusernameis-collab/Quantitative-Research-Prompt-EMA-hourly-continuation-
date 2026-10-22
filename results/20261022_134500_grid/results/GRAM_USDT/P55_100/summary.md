# EMA Hourly Continuation — GRAM/USDT P55_100

**Symbol:** GRAM/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 632 |
| net_profit_factor | 0.3855 |
| net_win_rate | 0.4446 |
| gross_profit_factor | 0.8884 |
| gross_win_rate | 0.4715 |
| sharpe_ratio | -6.8897 |
| sortino_ratio | -2.4416 |
| max_drawdown | 0.9580 |
| cagr | -0.7109 |
| net_avg_win | 21.3358 |
| net_avg_loss | -44.3088 |
| avg_hold_time_bars | 5.0364 |
| exposure | 0.1447 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
