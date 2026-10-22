# EMA Hourly Continuation — SAND/USDT P34_55

**Symbol:** SAND/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 827 |
| net_profit_factor | 0.3974 |
| net_win_rate | 0.4341 |
| gross_profit_factor | 0.8523 |
| gross_win_rate | 0.4522 |
| sharpe_ratio | -8.3225 |
| sortino_ratio | -3.3928 |
| max_drawdown | 0.9872 |
| cagr | -0.8192 |
| net_avg_win | 18.1207 |
| net_avg_loss | -34.9765 |
| avg_hold_time_bars | 3.2019 |
| exposure | 0.1204 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
