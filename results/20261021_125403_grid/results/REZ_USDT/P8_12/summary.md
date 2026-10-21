# EMA Hourly Continuation — REZ/USDT P8_12

**Symbol:** REZ/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 359 |
| net_profit_factor | 0.7148 |
| net_win_rate | 0.4903 |
| gross_profit_factor | 0.9719 |
| gross_win_rate | 0.4903 |
| sharpe_ratio | -2.1620 |
| sortino_ratio | -0.5906 |
| max_drawdown | 0.5202 |
| cagr | -0.2389 |
| net_avg_win | 69.9258 |
| net_avg_loss | -94.0863 |
| avg_hold_time_bars | 4.8830 |
| exposure | 0.0809 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
