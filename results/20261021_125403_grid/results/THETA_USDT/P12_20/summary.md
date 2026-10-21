# EMA Hourly Continuation — THETA/USDT P12_20

**Symbol:** THETA/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 277 |
| net_profit_factor | 0.7473 |
| net_win_rate | 0.5054 |
| gross_profit_factor | 1.0338 |
| gross_win_rate | 0.5054 |
| sharpe_ratio | -1.5926 |
| sortino_ratio | -0.3813 |
| max_drawdown | 0.3952 |
| cagr | -0.1601 |
| net_avg_win | 74.9285 |
| net_avg_loss | -102.4592 |
| avg_hold_time_bars | 5.2130 |
| exposure | 0.0656 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
