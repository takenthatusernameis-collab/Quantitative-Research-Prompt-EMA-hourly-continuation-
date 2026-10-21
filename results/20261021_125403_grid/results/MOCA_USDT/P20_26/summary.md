# EMA Hourly Continuation — MOCA/USDT P20_26

**Symbol:** MOCA/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 217 |
| net_profit_factor | 0.5724 |
| net_win_rate | 0.4608 |
| gross_profit_factor | 0.8549 |
| gross_win_rate | 0.4608 |
| sharpe_ratio | -2.6808 |
| sortino_ratio | -0.5932 |
| max_drawdown | 0.4925 |
| cagr | -0.2376 |
| net_avg_win | 61.6797 |
| net_avg_loss | -92.1050 |
| avg_hold_time_bars | 4.4286 |
| exposure | 0.0482 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
