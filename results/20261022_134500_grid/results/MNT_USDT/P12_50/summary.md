# EMA Hourly Continuation — MNT/USDT P12_50

**Symbol:** MNT/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 971 |
| net_profit_factor | 0.3538 |
| net_win_rate | 0.4346 |
| gross_profit_factor | 0.7119 |
| gross_win_rate | 0.4531 |
| sharpe_ratio | -8.3248 |
| sortino_ratio | -3.6237 |
| max_drawdown | 0.9907 |
| cagr | -0.8436 |
| net_avg_win | 12.8509 |
| net_avg_loss | -27.9205 |
| avg_hold_time_bars | 8.8363 |
| exposure | 0.3900 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
