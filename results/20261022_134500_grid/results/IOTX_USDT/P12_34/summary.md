# EMA Hourly Continuation — IOTX/USDT P12_34

**Symbol:** IOTX/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1247 |
| net_profit_factor | 0.5453 |
| net_win_rate | 0.4667 |
| gross_profit_factor | 0.9768 |
| gross_win_rate | 0.4779 |
| sharpe_ratio | -8.1156 |
| sortino_ratio | -4.0401 |
| max_drawdown | 0.9934 |
| cagr | -0.8629 |
| net_avg_win | 20.4651 |
| net_avg_loss | -32.8460 |
| avg_hold_time_bars | 4.4242 |
| exposure | 0.2508 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
