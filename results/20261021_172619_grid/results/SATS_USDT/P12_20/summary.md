# EMA Hourly Continuation — SATS/USDT P12_20

**Symbol:** SATS/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 362 |
| net_profit_factor | 0.7513 |
| net_win_rate | 0.5110 |
| gross_profit_factor | 1.0420 |
| gross_win_rate | 0.5110 |
| sharpe_ratio | -1.6920 |
| sortino_ratio | -0.4607 |
| max_drawdown | 0.4551 |
| cagr | -0.1921 |
| net_avg_win | 67.9658 |
| net_avg_loss | -94.5473 |
| avg_hold_time_bars | 4.8564 |
| exposure | 0.0796 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
