# EMA Hourly Continuation — MASK/USDT P20_55

**Symbol:** MASK/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 990 |
| net_profit_factor | 0.4189 |
| net_win_rate | 0.4444 |
| gross_profit_factor | 0.8588 |
| gross_win_rate | 0.4727 |
| sharpe_ratio | -7.8642 |
| sortino_ratio | -3.4818 |
| max_drawdown | 0.9878 |
| cagr | -0.8229 |
| net_avg_win | 16.1724 |
| net_avg_loss | -30.8843 |
| avg_hold_time_bars | 5.6616 |
| exposure | 0.2548 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
