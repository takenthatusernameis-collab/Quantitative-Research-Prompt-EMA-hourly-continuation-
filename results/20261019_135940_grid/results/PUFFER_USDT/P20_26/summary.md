# EMA Hourly Continuation — PUFFER/USDT P20_26

**Symbol:** PUFFER/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 889 |
| net_profit_factor | 0.3286 |
| net_win_rate | 0.4106 |
| gross_profit_factor | 0.6352 |
| gross_win_rate | 0.4331 |
| sharpe_ratio | -10.5841 |
| sortino_ratio | -4.9818 |
| max_drawdown | 0.9945 |
| cagr | -0.9243 |
| net_avg_win | 13.3360 |
| net_avg_loss | -28.2687 |
| avg_hold_time_bars | 2.5647 |
| exposure | 0.1290 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
