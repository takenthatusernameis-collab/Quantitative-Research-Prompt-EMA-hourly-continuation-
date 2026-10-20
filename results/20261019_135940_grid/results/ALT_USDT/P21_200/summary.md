# EMA Hourly Continuation — ALT/USDT P21_200

**Symbol:** ALT/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 366 |
| net_profit_factor | 0.7025 |
| net_win_rate | 0.4727 |
| gross_profit_factor | 0.9042 |
| gross_win_rate | 0.4781 |
| sharpe_ratio | -2.1289 |
| sortino_ratio | -0.5754 |
| max_drawdown | 0.5204 |
| cagr | -0.2366 |
| net_avg_win | 67.2135 |
| net_avg_loss | -85.7628 |
| avg_hold_time_bars | 38.6639 |
| exposure | 0.6432 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
