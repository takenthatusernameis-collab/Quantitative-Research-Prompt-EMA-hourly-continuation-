# EMA Hourly Continuation — LISTA/USDT P34_50

**Symbol:** LISTA/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 373 |
| net_profit_factor | 0.5896 |
| net_win_rate | 0.4504 |
| gross_profit_factor | 0.8203 |
| gross_win_rate | 0.4504 |
| sharpe_ratio | -3.3464 |
| sortino_ratio | -0.9551 |
| max_drawdown | 0.6476 |
| cagr | -0.3540 |
| net_avg_win | 54.6810 |
| net_avg_loss | -76.0028 |
| avg_hold_time_bars | 6.2413 |
| exposure | 0.1138 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
