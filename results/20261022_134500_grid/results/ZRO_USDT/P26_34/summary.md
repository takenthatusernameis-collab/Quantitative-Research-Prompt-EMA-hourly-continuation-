# EMA Hourly Continuation — ZRO/USDT P26_34

**Symbol:** ZRO/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1064 |
| net_profit_factor | 0.3798 |
| net_win_rate | 0.4079 |
| gross_profit_factor | 0.8276 |
| gross_win_rate | 0.4305 |
| sharpe_ratio | -10.9520 |
| sortino_ratio | -5.2557 |
| max_drawdown | 0.9981 |
| cagr | -0.9325 |
| net_avg_win | 14.0834 |
| net_avg_loss | -25.5453 |
| avg_hold_time_bars | 2.0498 |
| exposure | 0.1067 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
