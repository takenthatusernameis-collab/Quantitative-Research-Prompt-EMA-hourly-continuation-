# EMA Hourly Continuation — BAND/USDT P8_144

**Symbol:** BAND/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 400 |
| net_profit_factor | 0.7351 |
| net_win_rate | 0.4700 |
| gross_profit_factor | 0.8990 |
| gross_win_rate | 0.4700 |
| sharpe_ratio | -2.1180 |
| sortino_ratio | -0.5991 |
| max_drawdown | 0.5356 |
| cagr | -0.2424 |
| net_avg_win | 74.3103 |
| net_avg_loss | -89.6478 |
| avg_hold_time_bars | 40.9175 |
| exposure | 0.7406 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
