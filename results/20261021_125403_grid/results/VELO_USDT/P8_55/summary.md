# EMA Hourly Continuation — VELO/USDT P8_55

**Symbol:** VELO/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 692 |
| net_profit_factor | 0.8251 |
| net_win_rate | 0.5043 |
| gross_profit_factor | 0.9870 |
| gross_win_rate | 0.5043 |
| sharpe_ratio | -1.4089 |
| sortino_ratio | -0.5309 |
| max_drawdown | 0.5306 |
| cagr | -0.2197 |
| net_avg_win | 62.6939 |
| net_avg_loss | -77.3090 |
| avg_hold_time_bars | 12.9812 |
| exposure | 0.4083 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
