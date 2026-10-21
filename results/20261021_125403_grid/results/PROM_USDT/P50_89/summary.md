# EMA Hourly Continuation — PROM/USDT P50_89

**Symbol:** PROM/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 399 |
| net_profit_factor | 0.6193 |
| net_win_rate | 0.4737 |
| gross_profit_factor | 0.9141 |
| gross_win_rate | 0.4762 |
| sharpe_ratio | -2.9553 |
| sortino_ratio | -0.8415 |
| max_drawdown | 0.6309 |
| cagr | -0.3214 |
| net_avg_win | 53.5726 |
| net_avg_loss | -77.8519 |
| avg_hold_time_bars | 7.6867 |
| exposure | 0.1394 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
