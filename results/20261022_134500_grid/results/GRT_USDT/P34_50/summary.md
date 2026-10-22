# EMA Hourly Continuation — GRT/USDT P34_50

**Symbol:** GRT/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 912 |
| net_profit_factor | 0.3396 |
| net_win_rate | 0.4101 |
| gross_profit_factor | 0.7086 |
| gross_win_rate | 0.4386 |
| sharpe_ratio | -9.5024 |
| sortino_ratio | -4.0855 |
| max_drawdown | 0.9946 |
| cagr | -0.8723 |
| net_avg_win | 13.6705 |
| net_avg_loss | -27.9872 |
| avg_hold_time_bars | 2.5724 |
| exposure | 0.1062 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
