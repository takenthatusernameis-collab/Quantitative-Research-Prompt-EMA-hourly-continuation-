# EMA Hourly Continuation — MNT/USDT P50_144

**Symbol:** MNT/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 395 |
| net_profit_factor | 0.4469 |
| net_win_rate | 0.4380 |
| gross_profit_factor | 0.8312 |
| gross_win_rate | 0.4582 |
| sharpe_ratio | -4.3940 |
| sortino_ratio | -1.2260 |
| max_drawdown | 0.7926 |
| cagr | -0.4561 |
| net_avg_win | 36.5837 |
| net_avg_loss | -63.7937 |
| avg_hold_time_bars | 17.9975 |
| exposure | 0.3231 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
