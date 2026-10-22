# EMA Hourly Continuation — FLUX/USDT P55_200

**Symbol:** FLUX/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 280 |
| net_profit_factor | 1.0215 |
| net_win_rate | 0.5571 |
| gross_profit_factor | 1.2464 |
| gross_win_rate | 0.5571 |
| sharpe_ratio | 0.1599 |
| sortino_ratio | 0.0389 |
| max_drawdown | 0.1061 |
| cagr | 0.0114 |
| net_avg_win | 87.6628 |
| net_avg_loss | -107.9634 |
| avg_hold_time_bars | 30.1536 |
| exposure | 0.3838 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
