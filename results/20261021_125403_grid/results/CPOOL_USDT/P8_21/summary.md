# EMA Hourly Continuation — CPOOL/USDT P8_21

**Symbol:** CPOOL/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 503 |
| net_profit_factor | 0.7504 |
| net_win_rate | 0.4732 |
| gross_profit_factor | 0.9312 |
| gross_win_rate | 0.4732 |
| sharpe_ratio | -2.3635 |
| sortino_ratio | -0.7550 |
| max_drawdown | 0.5926 |
| cagr | -0.2941 |
| net_avg_win | 73.6304 |
| net_avg_loss | -88.1269 |
| avg_hold_time_bars | 6.1074 |
| exposure | 0.1396 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
