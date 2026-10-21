# EMA Hourly Continuation — IOTX/USDT P50_55

**Symbol:** IOTX/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 145 |
| net_profit_factor | 0.6488 |
| net_win_rate | 0.4828 |
| gross_profit_factor | 0.9568 |
| gross_win_rate | 0.4828 |
| sharpe_ratio | -1.7123 |
| sortino_ratio | -0.2959 |
| max_drawdown | 0.3342 |
| cagr | -0.1263 |
| net_avg_win | 75.8867 |
| net_avg_loss | -109.1666 |
| avg_hold_time_bars | 5.0276 |
| exposure | 0.0331 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
