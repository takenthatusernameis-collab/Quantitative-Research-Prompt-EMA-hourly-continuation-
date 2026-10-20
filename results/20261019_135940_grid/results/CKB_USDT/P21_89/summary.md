# EMA Hourly Continuation — CKB/USDT P21_89

**Symbol:** CKB/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 761 |
| net_profit_factor | 0.6001 |
| net_win_rate | 0.4507 |
| gross_profit_factor | 0.8976 |
| gross_win_rate | 0.4639 |
| sharpe_ratio | -5.2306 |
| sortino_ratio | -2.0306 |
| max_drawdown | 0.9152 |
| cagr | -0.6238 |
| net_avg_win | 39.9993 |
| net_avg_loss | -54.6913 |
| avg_hold_time_bars | 10.4284 |
| exposure | 0.3607 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
