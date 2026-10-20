# EMA Hourly Continuation — UQC/USDT P26_55

**Symbol:** UQC/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 400 |
| net_profit_factor | 0.1379 |
| net_win_rate | 0.2625 |
| gross_profit_factor | 0.3479 |
| gross_win_rate | 0.2700 |
| sharpe_ratio | -9.1600 |
| sortino_ratio | -2.6095 |
| max_drawdown | 0.9729 |
| cagr | -0.7608 |
| net_avg_win | 14.8183 |
| net_avg_loss | -38.2536 |
| avg_hold_time_bars | 28.3400 |
| exposure | 0.5131 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
