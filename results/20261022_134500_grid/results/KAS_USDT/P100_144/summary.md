# EMA Hourly Continuation — KAS/USDT P100_144

**Symbol:** KAS/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 529 |
| net_profit_factor | 0.2912 |
| net_win_rate | 0.4140 |
| gross_profit_factor | 0.6441 |
| gross_win_rate | 0.4367 |
| sharpe_ratio | -6.8855 |
| sortino_ratio | -2.2360 |
| max_drawdown | 0.9459 |
| cagr | -0.6826 |
| net_avg_win | 17.7048 |
| net_avg_loss | -42.9582 |
| avg_hold_time_bars | 3.6843 |
| exposure | 0.0886 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
