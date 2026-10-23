# EMA Hourly Continuation — ANKR/USDT P21_55

**Symbol:** ANKR/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 965 |
| net_profit_factor | 0.5159 |
| net_win_rate | 0.4238 |
| gross_profit_factor | 0.9078 |
| gross_win_rate | 0.4415 |
| sharpe_ratio | -8.3191 |
| sortino_ratio | -3.6324 |
| max_drawdown | 0.9898 |
| cagr | -0.8365 |
| net_avg_win | 25.7839 |
| net_avg_loss | -36.7620 |
| avg_hold_time_bars | 6.0415 |
| exposure | 0.2650 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
