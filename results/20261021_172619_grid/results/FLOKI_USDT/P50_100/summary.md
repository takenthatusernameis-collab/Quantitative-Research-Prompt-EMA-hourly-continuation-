# EMA Hourly Continuation — FLOKI/USDT P50_100

**Symbol:** FLOKI/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 381 |
| net_profit_factor | 0.8373 |
| net_win_rate | 0.5223 |
| gross_profit_factor | 1.0833 |
| gross_win_rate | 0.5223 |
| sharpe_ratio | -1.0386 |
| sortino_ratio | -0.2923 |
| max_drawdown | 0.3019 |
| cagr | -0.1269 |
| net_avg_win | 74.6927 |
| net_avg_loss | -97.5350 |
| avg_hold_time_bars | 9.4409 |
| exposure | 0.1635 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
