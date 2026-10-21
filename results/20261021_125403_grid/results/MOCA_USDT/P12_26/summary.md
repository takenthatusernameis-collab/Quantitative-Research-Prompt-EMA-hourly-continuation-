# EMA Hourly Continuation — MOCA/USDT P12_26

**Symbol:** MOCA/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 479 |
| net_profit_factor | 0.6228 |
| net_win_rate | 0.4676 |
| gross_profit_factor | 0.8774 |
| gross_win_rate | 0.4676 |
| sharpe_ratio | -3.4792 |
| sortino_ratio | -1.1425 |
| max_drawdown | 0.7056 |
| cagr | -0.4069 |
| net_avg_win | 51.2810 |
| net_avg_loss | -72.3287 |
| avg_hold_time_bars | 5.4906 |
| exposure | 0.1318 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
