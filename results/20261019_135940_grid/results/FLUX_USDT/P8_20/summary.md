# EMA Hourly Continuation — FLUX/USDT P8_20

**Symbol:** FLUX/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1639 |
| net_profit_factor | 0.4678 |
| net_win_rate | 0.4503 |
| gross_profit_factor | 1.0209 |
| gross_win_rate | 0.4771 |
| sharpe_ratio | -10.7373 |
| sortino_ratio | -6.1208 |
| max_drawdown | 0.9996 |
| cagr | -0.9545 |
| net_avg_win | 11.9056 |
| net_avg_loss | -20.8458 |
| avg_hold_time_bars | 2.7846 |
| exposure | 0.2075 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
