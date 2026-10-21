# EMA Hourly Continuation — ZBCN/USDT P89_200

**Symbol:** ZBCN/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 275 |
| net_profit_factor | 0.8321 |
| net_win_rate | 0.5018 |
| gross_profit_factor | 0.9871 |
| gross_win_rate | 0.5018 |
| sharpe_ratio | -0.8645 |
| sortino_ratio | -0.2072 |
| max_drawdown | 0.2790 |
| cagr | -0.0925 |
| net_avg_win | 76.5005 |
| net_avg_loss | -92.6094 |
| avg_hold_time_bars | 12.8145 |
| exposure | 0.1630 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
