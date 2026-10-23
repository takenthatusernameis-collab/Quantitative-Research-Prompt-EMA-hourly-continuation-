# EMA Hourly Continuation — DUSK/USDT P89_100

**Symbol:** DUSK/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 580 |
| net_profit_factor | 0.3160 |
| net_win_rate | 0.4121 |
| gross_profit_factor | 0.7938 |
| gross_win_rate | 0.4397 |
| sharpe_ratio | -7.7764 |
| sortino_ratio | -2.6651 |
| max_drawdown | 0.9675 |
| cagr | -0.7446 |
| net_avg_win | 18.7053 |
| net_avg_loss | -41.4841 |
| avg_hold_time_bars | 2.2414 |
| exposure | 0.0591 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
