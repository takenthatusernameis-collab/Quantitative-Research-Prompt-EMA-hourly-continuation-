# EMA Hourly Continuation — CATI/USDT P8_55

**Symbol:** CATI/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 893 |
| net_profit_factor | 0.5346 |
| net_win_rate | 0.4289 |
| gross_profit_factor | 0.8186 |
| gross_win_rate | 0.4434 |
| sharpe_ratio | -7.5019 |
| sortino_ratio | -3.4650 |
| max_drawdown | 0.9721 |
| cagr | -0.8124 |
| net_avg_win | 29.0688 |
| net_avg_loss | -40.8366 |
| avg_hold_time_bars | 9.8835 |
| exposure | 0.4838 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
