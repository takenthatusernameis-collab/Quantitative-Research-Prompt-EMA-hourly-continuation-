# EMA Hourly Continuation — ZBCN/USDT P34_100

**Symbol:** ZBCN/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 416 |
| net_profit_factor | 0.7340 |
| net_win_rate | 0.4736 |
| gross_profit_factor | 0.8829 |
| gross_win_rate | 0.4736 |
| sharpe_ratio | -1.8805 |
| sortino_ratio | -0.5503 |
| max_drawdown | 0.5088 |
| cagr | -0.2238 |
| net_avg_win | 65.0835 |
| net_avg_loss | -79.7657 |
| avg_hold_time_bars | 10.2428 |
| exposure | 0.1971 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
