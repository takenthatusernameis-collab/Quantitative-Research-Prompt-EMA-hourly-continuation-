# EMA Hourly Continuation — LPT/USDT P8_12

**Symbol:** LPT/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 355 |
| net_profit_factor | 0.6240 |
| net_win_rate | 0.5014 |
| gross_profit_factor | 0.9662 |
| gross_win_rate | 0.5014 |
| sharpe_ratio | -2.6466 |
| sortino_ratio | -0.7170 |
| max_drawdown | 0.5729 |
| cagr | -0.2778 |
| net_avg_win | 52.0528 |
| net_avg_loss | -83.8953 |
| avg_hold_time_bars | 4.3887 |
| exposure | 0.0708 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
