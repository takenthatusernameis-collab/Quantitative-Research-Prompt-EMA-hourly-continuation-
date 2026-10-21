# EMA Hourly Continuation — ALT/USDT P20_21

**Symbol:** ALT/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 301 |
| net_profit_factor | 0.6081 |
| net_win_rate | 0.4751 |
| gross_profit_factor | 0.8907 |
| gross_win_rate | 0.4751 |
| sharpe_ratio | -2.6091 |
| sortino_ratio | -0.6486 |
| max_drawdown | 0.5513 |
| cagr | -0.2574 |
| net_avg_win | 57.1162 |
| net_avg_loss | -85.0094 |
| avg_hold_time_bars | 5.6910 |
| exposure | 0.0779 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
