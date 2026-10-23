# EMA Hourly Continuation — ALPINE/USDT P21_89

**Symbol:** ALPINE/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 747 |
| net_profit_factor | 0.5068 |
| net_win_rate | 0.4297 |
| gross_profit_factor | 0.8139 |
| gross_win_rate | 0.4418 |
| sharpe_ratio | -6.3320 |
| sortino_ratio | -2.4207 |
| max_drawdown | 0.9505 |
| cagr | -0.6942 |
| net_avg_win | 30.3818 |
| net_avg_loss | -45.1697 |
| avg_hold_time_bars | 11.1794 |
| exposure | 0.3796 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
