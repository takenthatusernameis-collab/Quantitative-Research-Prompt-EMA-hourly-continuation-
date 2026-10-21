# EMA Hourly Continuation — PEPE/USDT P50_89

**Symbol:** PEPE/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 314 |
| net_profit_factor | 0.7642 |
| net_win_rate | 0.4936 |
| gross_profit_factor | 0.9737 |
| gross_win_rate | 0.4936 |
| sharpe_ratio | -1.5125 |
| sortino_ratio | -0.3837 |
| max_drawdown | 0.3806 |
| cagr | -0.1617 |
| net_avg_win | 74.8293 |
| net_avg_loss | -95.4506 |
| avg_hold_time_bars | 7.2389 |
| exposure | 0.1033 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
