# EMA Hourly Continuation — SWFTC/USDT P12_21

**Symbol:** SWFTC/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1417 |
| net_profit_factor | 0.1900 |
| net_win_rate | 0.3557 |
| gross_profit_factor | 0.5326 |
| gross_win_rate | 0.3888 |
| sharpe_ratio | -15.3759 |
| sortino_ratio | -8.3098 |
| max_drawdown | 1.0000 |
| cagr | -0.9885 |
| net_avg_win | 4.6552 |
| net_avg_loss | -13.5226 |
| avg_hold_time_bars | 2.5131 |
| exposure | 0.1619 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
