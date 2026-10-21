# EMA Hourly Continuation — FIDA/USDT P50_89

**Symbol:** FIDA/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 422 |
| net_profit_factor | 0.5379 |
| net_win_rate | 0.4384 |
| gross_profit_factor | 0.7458 |
| gross_win_rate | 0.4384 |
| sharpe_ratio | -3.6600 |
| sortino_ratio | -1.0672 |
| max_drawdown | 0.7155 |
| cagr | -0.3878 |
| net_avg_win | 44.6778 |
| net_avg_loss | -64.8318 |
| avg_hold_time_bars | 6.9005 |
| exposure | 0.1318 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
