# EMA Hourly Continuation — STRAX/USDT P12_100

**Symbol:** STRAX/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 808 |
| net_profit_factor | 0.6021 |
| net_win_rate | 0.4431 |
| gross_profit_factor | 0.9022 |
| gross_win_rate | 0.4567 |
| sharpe_ratio | -5.7087 |
| sortino_ratio | -2.2846 |
| max_drawdown | 0.9365 |
| cagr | -0.6663 |
| net_avg_win | 39.5308 |
| net_avg_loss | -52.2361 |
| avg_hold_time_bars | 14.5990 |
| exposure | 0.5393 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
