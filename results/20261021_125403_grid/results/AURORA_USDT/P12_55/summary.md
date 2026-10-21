# EMA Hourly Continuation — AURORA/USDT P12_55

**Symbol:** AURORA/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 576 |
| net_profit_factor | 0.6249 |
| net_win_rate | 0.4497 |
| gross_profit_factor | 0.8523 |
| gross_win_rate | 0.4497 |
| sharpe_ratio | -3.9959 |
| sortino_ratio | -1.3605 |
| max_drawdown | 0.8048 |
| cagr | -0.4700 |
| net_avg_win | 51.2746 |
| net_avg_loss | -67.0345 |
| avg_hold_time_bars | 13.1354 |
| exposure | 0.3439 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
