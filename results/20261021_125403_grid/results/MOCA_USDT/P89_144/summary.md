# EMA Hourly Continuation — MOCA/USDT P89_144

**Symbol:** MOCA/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 244 |
| net_profit_factor | 0.6715 |
| net_win_rate | 0.4754 |
| gross_profit_factor | 0.9068 |
| gross_win_rate | 0.4754 |
| sharpe_ratio | -2.0891 |
| sortino_ratio | -0.4890 |
| max_drawdown | 0.4187 |
| cagr | -0.2022 |
| net_avg_win | 70.8481 |
| net_avg_loss | -95.6188 |
| avg_hold_time_bars | 8.4713 |
| exposure | 0.1036 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
