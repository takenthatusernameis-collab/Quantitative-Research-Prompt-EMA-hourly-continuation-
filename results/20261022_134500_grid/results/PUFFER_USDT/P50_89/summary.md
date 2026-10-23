# EMA Hourly Continuation — PUFFER/USDT P50_89

**Symbol:** PUFFER/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 499 |
| net_profit_factor | 0.5012 |
| net_win_rate | 0.4329 |
| gross_profit_factor | 0.7973 |
| gross_win_rate | 0.4469 |
| sharpe_ratio | -5.2158 |
| sortino_ratio | -1.8362 |
| max_drawdown | 0.8339 |
| cagr | -0.5820 |
| net_avg_win | 38.5086 |
| net_avg_loss | -58.6451 |
| avg_hold_time_bars | 6.3527 |
| exposure | 0.1794 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
