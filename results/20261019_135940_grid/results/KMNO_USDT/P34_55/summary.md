# EMA Hourly Continuation — KMNO/USDT P34_55

**Symbol:** KMNO/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 761 |
| net_profit_factor | 0.4855 |
| net_win_rate | 0.4468 |
| gross_profit_factor | 0.8662 |
| gross_win_rate | 0.4639 |
| sharpe_ratio | -6.8880 |
| sortino_ratio | -2.7022 |
| max_drawdown | 0.9651 |
| cagr | -0.7379 |
| net_avg_win | 26.7444 |
| net_avg_loss | -44.4851 |
| avg_hold_time_bars | 3.5453 |
| exposure | 0.1246 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
