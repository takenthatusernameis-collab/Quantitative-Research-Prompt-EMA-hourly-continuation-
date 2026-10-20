# EMA Hourly Continuation — XPR/USDT P20_100

**Symbol:** XPR/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 743 |
| net_profit_factor | 0.4484 |
| net_win_rate | 0.4159 |
| gross_profit_factor | 0.7896 |
| gross_win_rate | 0.4253 |
| sharpe_ratio | -7.4449 |
| sortino_ratio | -2.8192 |
| max_drawdown | 0.9749 |
| cagr | -0.7668 |
| net_avg_win | 25.6286 |
| net_avg_loss | -40.6931 |
| avg_hold_time_bars | 9.6595 |
| exposure | 0.3262 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
