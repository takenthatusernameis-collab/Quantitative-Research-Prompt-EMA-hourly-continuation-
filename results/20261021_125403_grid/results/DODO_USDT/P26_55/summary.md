# EMA Hourly Continuation — DODO/USDT P26_55

**Symbol:** DODO/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 519 |
| net_profit_factor | 0.6333 |
| net_win_rate | 0.4528 |
| gross_profit_factor | 0.8514 |
| gross_win_rate | 0.4528 |
| sharpe_ratio | -3.5216 |
| sortino_ratio | -1.1402 |
| max_drawdown | 0.7458 |
| cagr | -0.4070 |
| net_avg_win | 53.8203 |
| net_avg_loss | -70.3218 |
| avg_hold_time_bars | 6.3834 |
| exposure | 0.1499 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
