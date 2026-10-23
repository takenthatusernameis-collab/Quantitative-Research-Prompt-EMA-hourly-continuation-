# EMA Hourly Continuation — WEMIX/USDT P50_200

**Symbol:** WEMIX/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 655 |
| net_profit_factor | 0.3490 |
| net_win_rate | 0.3099 |
| gross_profit_factor | 0.5344 |
| gross_win_rate | 0.3191 |
| sharpe_ratio | -9.5725 |
| sortino_ratio | -3.4561 |
| max_drawdown | 0.9875 |
| cagr | -0.8248 |
| net_avg_win | 26.0759 |
| net_avg_loss | -33.5564 |
| avg_hold_time_bars | 14.2534 |
| exposure | 0.4244 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
