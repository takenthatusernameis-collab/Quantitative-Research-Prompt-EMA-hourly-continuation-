# EMA Hourly Continuation — CKB/USDT P21_26

**Symbol:** CKB/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1202 |
| net_profit_factor | 0.1954 |
| net_win_rate | 0.3494 |
| gross_profit_factor | 0.5276 |
| gross_win_rate | 0.4093 |
| sharpe_ratio | -14.9767 |
| sortino_ratio | -7.5886 |
| max_drawdown | 1.0000 |
| cagr | -0.9821 |
| net_avg_win | 5.7806 |
| net_avg_loss | -15.8919 |
| avg_hold_time_bars | 1.9792 |
| exposure | 0.1081 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
