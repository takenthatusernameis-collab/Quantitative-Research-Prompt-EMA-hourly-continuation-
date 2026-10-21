# EMA Hourly Continuation — PHA/USDT P8_34

**Symbol:** PHA/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 749 |
| net_profit_factor | 0.7905 |
| net_win_rate | 0.4967 |
| gross_profit_factor | 0.9899 |
| gross_win_rate | 0.4967 |
| sharpe_ratio | -2.0437 |
| sortino_ratio | -0.8004 |
| max_drawdown | 0.6388 |
| cagr | -0.3091 |
| net_avg_win | 61.3546 |
| net_avg_loss | -76.5870 |
| avg_hold_time_bars | 8.7116 |
| exposure | 0.2966 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
