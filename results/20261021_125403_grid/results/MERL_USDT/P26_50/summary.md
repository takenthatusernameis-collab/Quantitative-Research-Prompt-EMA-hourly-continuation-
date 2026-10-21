# EMA Hourly Continuation — MERL/USDT P26_50

**Symbol:** MERL/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 415 |
| net_profit_factor | 0.7433 |
| net_win_rate | 0.4867 |
| gross_profit_factor | 0.9430 |
| gross_win_rate | 0.4867 |
| sharpe_ratio | -1.8613 |
| sortino_ratio | -0.5425 |
| max_drawdown | 0.4970 |
| cagr | -0.2207 |
| net_avg_win | 66.5770 |
| net_avg_loss | -84.9449 |
| avg_hold_time_bars | 7.0723 |
| exposure | 0.1338 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
