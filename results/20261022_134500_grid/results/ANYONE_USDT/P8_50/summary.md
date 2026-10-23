# EMA Hourly Continuation — ANYONE/USDT P8_50

**Symbol:** ANYONE/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 991 |
| net_profit_factor | 0.6470 |
| net_win_rate | 0.4511 |
| gross_profit_factor | 0.8720 |
| gross_win_rate | 0.4541 |
| sharpe_ratio | -5.0364 |
| sortino_ratio | -2.3544 |
| max_drawdown | 0.9209 |
| cagr | -0.6712 |
| net_avg_win | 37.6825 |
| net_avg_loss | -47.8555 |
| avg_hold_time_bars | 9.2412 |
| exposure | 0.4628 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
