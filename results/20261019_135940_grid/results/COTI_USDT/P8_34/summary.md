# EMA Hourly Continuation — COTI/USDT P8_34

**Symbol:** COTI/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1458 |
| net_profit_factor | 0.5604 |
| net_win_rate | 0.4403 |
| gross_profit_factor | 0.9212 |
| gross_win_rate | 0.4486 |
| sharpe_ratio | -8.5252 |
| sortino_ratio | -4.5619 |
| max_drawdown | 0.9966 |
| cagr | -0.8934 |
| net_avg_win | 19.7837 |
| net_avg_loss | -27.7757 |
| avg_hold_time_bars | 4.9678 |
| exposure | 0.3292 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
