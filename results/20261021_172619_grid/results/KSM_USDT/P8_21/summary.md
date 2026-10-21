# EMA Hourly Continuation — KSM/USDT P8_21

**Symbol:** KSM/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 666 |
| net_profit_factor | 0.6287 |
| net_win_rate | 0.4700 |
| gross_profit_factor | 0.9136 |
| gross_win_rate | 0.4700 |
| sharpe_ratio | -4.0542 |
| sortino_ratio | -1.4977 |
| max_drawdown | 0.8231 |
| cagr | -0.4963 |
| net_avg_win | 44.4317 |
| net_avg_loss | -62.6638 |
| avg_hold_time_bars | 5.5435 |
| exposure | 0.1678 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
