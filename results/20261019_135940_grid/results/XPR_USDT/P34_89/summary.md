# EMA Hourly Continuation — XPR/USDT P34_89

**Symbol:** XPR/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 696 |
| net_profit_factor | 0.3703 |
| net_win_rate | 0.4023 |
| gross_profit_factor | 0.7418 |
| gross_win_rate | 0.4138 |
| sharpe_ratio | -8.1729 |
| sortino_ratio | -3.0350 |
| max_drawdown | 0.9808 |
| cagr | -0.7898 |
| net_avg_win | 20.5857 |
| net_avg_loss | -37.4157 |
| avg_hold_time_bars | 6.1020 |
| exposure | 0.1930 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
