# EMA Hourly Continuation — IOTX/USDT P20_21

**Symbol:** IOTX/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 162 |
| net_profit_factor | 0.7013 |
| net_win_rate | 0.5123 |
| gross_profit_factor | 1.0396 |
| gross_win_rate | 0.5123 |
| sharpe_ratio | -1.3548 |
| sortino_ratio | -0.2487 |
| max_drawdown | 0.2558 |
| cagr | -0.1070 |
| net_avg_win | 70.0115 |
| net_avg_loss | -104.8810 |
| avg_hold_time_bars | 4.6481 |
| exposure | 0.0342 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
