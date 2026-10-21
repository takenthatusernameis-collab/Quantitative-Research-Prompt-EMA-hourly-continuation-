# EMA Hourly Continuation — BAND/USDT P50_100

**Symbol:** BAND/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 415 |
| net_profit_factor | 0.6345 |
| net_win_rate | 0.4530 |
| gross_profit_factor | 0.8671 |
| gross_win_rate | 0.4554 |
| sharpe_ratio | -3.2304 |
| sortino_ratio | -0.9342 |
| max_drawdown | 0.6696 |
| cagr | -0.3509 |
| net_avg_win | 61.2874 |
| net_avg_loss | -80.0011 |
| avg_hold_time_bars | 9.9084 |
| exposure | 0.1861 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
