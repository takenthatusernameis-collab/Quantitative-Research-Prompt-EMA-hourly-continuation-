# EMA Hourly Continuation — AURORA/USDT P34_100

**Symbol:** AURORA/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 357 |
| net_profit_factor | 0.6900 |
| net_win_rate | 0.4734 |
| gross_profit_factor | 0.9246 |
| gross_win_rate | 0.4734 |
| sharpe_ratio | -2.3980 |
| sortino_ratio | -0.6461 |
| max_drawdown | 0.5514 |
| cagr | -0.2565 |
| net_avg_win | 69.1376 |
| net_avg_loss | -90.0701 |
| avg_hold_time_bars | 17.2353 |
| exposure | 0.2797 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
