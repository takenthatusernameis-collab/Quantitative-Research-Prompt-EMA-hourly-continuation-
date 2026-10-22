# EMA Hourly Continuation — XMR/USDT P26_50

**Symbol:** XMR/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1330 |
| net_profit_factor | 0.2197 |
| net_win_rate | 0.3639 |
| gross_profit_factor | 0.6122 |
| gross_win_rate | 0.3895 |
| sharpe_ratio | -14.4061 |
| sortino_ratio | -7.5337 |
| max_drawdown | 1.0000 |
| cagr | -0.9814 |
| net_avg_win | 5.8182 |
| net_avg_loss | -15.1484 |
| avg_hold_time_bars | 2.4752 |
| exposure | 0.1496 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
