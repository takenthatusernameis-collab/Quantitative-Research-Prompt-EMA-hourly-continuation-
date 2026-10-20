# EMA Hourly Continuation — RIO/USDT P26_144

**Symbol:** RIO/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 617 |
| net_profit_factor | 0.5849 |
| net_win_rate | 0.4263 |
| gross_profit_factor | 0.7739 |
| gross_win_rate | 0.4279 |
| sharpe_ratio | -4.6602 |
| sortino_ratio | -1.6285 |
| max_drawdown | 0.8720 |
| cagr | -0.5438 |
| net_avg_win | 45.9753 |
| net_avg_loss | -58.3928 |
| avg_hold_time_bars | 15.7974 |
| exposure | 0.4475 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
