# EMA Hourly Continuation — HTR/USDT P21_34

**Symbol:** HTR/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1064 |
| net_profit_factor | 0.3169 |
| net_win_rate | 0.3402 |
| gross_profit_factor | 0.6092 |
| gross_win_rate | 0.3534 |
| sharpe_ratio | -12.1315 |
| sortino_ratio | -5.6103 |
| max_drawdown | 0.9993 |
| cagr | -0.9435 |
| net_avg_win | 12.8076 |
| net_avg_loss | -20.8390 |
| avg_hold_time_bars | 3.2867 |
| exposure | 0.1590 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
