# EMA Hourly Continuation — GRT/USDT P8_20

**Symbol:** GRT/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 516 |
| net_profit_factor | 0.6936 |
| net_win_rate | 0.4826 |
| gross_profit_factor | 0.9565 |
| gross_win_rate | 0.4826 |
| sharpe_ratio | -2.8674 |
| sortino_ratio | -0.9311 |
| max_drawdown | 0.6623 |
| cagr | -0.3476 |
| net_avg_win | 59.9587 |
| net_avg_loss | -80.6192 |
| avg_hold_time_bars | 5.4593 |
| exposure | 0.1275 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
