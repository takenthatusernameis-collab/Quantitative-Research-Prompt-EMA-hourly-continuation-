# EMA Hourly Continuation — FLIP/USDT P12_20

**Symbol:** FLIP/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 491 |
| net_profit_factor | 0.4268 |
| net_win_rate | 0.4033 |
| gross_profit_factor | 0.7662 |
| gross_win_rate | 0.4236 |
| sharpe_ratio | -6.7611 |
| sortino_ratio | -2.1307 |
| max_drawdown | 0.9320 |
| cagr | -0.6551 |
| net_avg_win | 35.0042 |
| net_avg_loss | -55.4283 |
| avg_hold_time_bars | 7.8208 |
| exposure | 0.1745 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
