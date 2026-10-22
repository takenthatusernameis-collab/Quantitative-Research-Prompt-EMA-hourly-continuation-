# EMA Hourly Continuation — IOTX/USDT P21_100

**Symbol:** IOTX/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 487 |
| net_profit_factor | 0.7384 |
| net_win_rate | 0.4908 |
| gross_profit_factor | 0.9360 |
| gross_win_rate | 0.4908 |
| sharpe_ratio | -1.9852 |
| sortino_ratio | -0.6261 |
| max_drawdown | 0.5684 |
| cagr | -0.2501 |
| net_avg_win | 60.7533 |
| net_avg_loss | -79.2960 |
| avg_hold_time_bars | 16.8747 |
| exposure | 0.3735 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
