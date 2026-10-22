# EMA Hourly Continuation — POKT/USDT P50_55

**Symbol:** POKT/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 210 |
| net_profit_factor | 0.3928 |
| net_win_rate | 0.3286 |
| gross_profit_factor | 0.5712 |
| gross_win_rate | 0.3333 |
| sharpe_ratio | -4.5566 |
| sortino_ratio | -0.9350 |
| max_drawdown | 0.6770 |
| cagr | -0.3563 |
| net_avg_win | 62.8859 |
| net_avg_loss | -78.3478 |
| avg_hold_time_bars | 6.9571 |
| exposure | 0.0661 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
