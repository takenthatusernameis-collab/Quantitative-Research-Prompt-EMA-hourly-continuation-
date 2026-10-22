# EMA Hourly Continuation — CTSI/USDT P12_21

**Symbol:** CTSI/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 534 |
| net_profit_factor | 0.6298 |
| net_win_rate | 0.4757 |
| gross_profit_factor | 0.9532 |
| gross_win_rate | 0.4757 |
| sharpe_ratio | -3.7562 |
| sortino_ratio | -1.2456 |
| max_drawdown | 0.7602 |
| cagr | -0.4337 |
| net_avg_win | 50.9277 |
| net_avg_loss | -73.3503 |
| avg_hold_time_bars | 4.9775 |
| exposure | 0.1208 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
