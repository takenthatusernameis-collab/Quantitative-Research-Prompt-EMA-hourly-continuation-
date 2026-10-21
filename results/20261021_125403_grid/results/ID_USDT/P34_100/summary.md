# EMA Hourly Continuation — ID/USDT P34_100

**Symbol:** ID/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 482 |
| net_profit_factor | 0.6725 |
| net_win_rate | 0.4689 |
| gross_profit_factor | 0.8846 |
| gross_win_rate | 0.4689 |
| sharpe_ratio | -2.7385 |
| sortino_ratio | -0.8549 |
| max_drawdown | 0.6357 |
| cagr | -0.3246 |
| net_avg_win | 57.1037 |
| net_avg_loss | -74.9577 |
| avg_hold_time_bars | 11.6286 |
| exposure | 0.2537 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
