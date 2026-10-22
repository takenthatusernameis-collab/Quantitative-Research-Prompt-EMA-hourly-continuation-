# EMA Hourly Continuation — SAND/USDT P34_200

**Symbol:** SAND/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 352 |
| net_profit_factor | 0.7064 |
| net_win_rate | 0.4972 |
| gross_profit_factor | 1.0384 |
| gross_win_rate | 0.5057 |
| sharpe_ratio | -2.0787 |
| sortino_ratio | -0.5491 |
| max_drawdown | 0.4955 |
| cagr | -0.2301 |
| net_avg_win | 66.2020 |
| net_avg_loss | -92.6526 |
| avg_hold_time_bars | 33.4091 |
| exposure | 0.5345 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
