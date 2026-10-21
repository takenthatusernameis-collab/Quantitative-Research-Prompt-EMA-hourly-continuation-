# EMA Hourly Continuation — SAND/USDT P8_21

**Symbol:** SAND/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 555 |
| net_profit_factor | 0.7102 |
| net_win_rate | 0.5027 |
| gross_profit_factor | 1.0084 |
| gross_win_rate | 0.5027 |
| sharpe_ratio | -2.5004 |
| sortino_ratio | -0.8470 |
| max_drawdown | 0.6254 |
| cagr | -0.3210 |
| net_avg_win | 54.6077 |
| net_avg_loss | -77.7304 |
| avg_hold_time_bars | 6.1802 |
| exposure | 0.1559 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
