# EMA Hourly Continuation — DOT/USDT P12_50

**Symbol:** DOT/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 970 |
| net_profit_factor | 0.5258 |
| net_win_rate | 0.4649 |
| gross_profit_factor | 0.9243 |
| gross_win_rate | 0.4784 |
| sharpe_ratio | -6.4705 |
| sortino_ratio | -2.8292 |
| max_drawdown | 0.9719 |
| cagr | -0.7514 |
| net_avg_win | 23.8426 |
| net_avg_loss | -39.4023 |
| avg_hold_time_bars | 8.9062 |
| exposure | 0.3927 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
