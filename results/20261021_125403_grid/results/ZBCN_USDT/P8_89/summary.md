# EMA Hourly Continuation — ZBCN/USDT P8_89

**Symbol:** ZBCN/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 584 |
| net_profit_factor | 0.9924 |
| net_win_rate | 0.5377 |
| gross_profit_factor | 1.1487 |
| gross_win_rate | 0.5377 |
| sharpe_ratio | 0.0148 |
| sortino_ratio | 0.0052 |
| max_drawdown | 0.2541 |
| cagr | -0.0095 |
| net_avg_win | 96.4468 |
| net_avg_loss | -113.0262 |
| avg_hold_time_bars | 20.1935 |
| exposure | 0.5456 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
