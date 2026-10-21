# EMA Hourly Continuation — AURORA/USDT P26_89

**Symbol:** AURORA/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 397 |
| net_profit_factor | 0.6978 |
| net_win_rate | 0.4736 |
| gross_profit_factor | 0.9267 |
| gross_win_rate | 0.4736 |
| sharpe_ratio | -2.4767 |
| sortino_ratio | -0.7034 |
| max_drawdown | 0.5881 |
| cagr | -0.2760 |
| net_avg_win | 68.2265 |
| net_avg_loss | -87.9521 |
| avg_hold_time_bars | 16.4610 |
| exposure | 0.2970 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
