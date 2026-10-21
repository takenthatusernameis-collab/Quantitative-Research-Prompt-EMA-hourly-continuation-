# EMA Hourly Continuation — XPR/USDT P55_89

**Symbol:** XPR/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 184 |
| net_profit_factor | 0.6533 |
| net_win_rate | 0.4728 |
| gross_profit_factor | 0.9094 |
| gross_win_rate | 0.4728 |
| sharpe_ratio | -1.8912 |
| sortino_ratio | -0.3666 |
| max_drawdown | 0.3573 |
| cagr | -0.1552 |
| net_avg_win | 74.7960 |
| net_avg_loss | -102.6821 |
| avg_hold_time_bars | 8.3804 |
| exposure | 0.0701 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
