# EMA Hourly Continuation — ROSE/USDT P50_89

**Symbol:** ROSE/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 683 |
| net_profit_factor | 0.5818 |
| net_win_rate | 0.4641 |
| gross_profit_factor | 0.9489 |
| gross_win_rate | 0.4729 |
| sharpe_ratio | -5.0180 |
| sortino_ratio | -1.8519 |
| max_drawdown | 0.8962 |
| cagr | -0.5891 |
| net_avg_win | 39.1792 |
| net_avg_loss | -58.3295 |
| avg_hold_time_bars | 4.9488 |
| exposure | 0.1536 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
