# EMA Hourly Continuation — CATI/USDT P8_34

**Symbol:** CATI/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 526 |
| net_profit_factor | 0.5984 |
| net_win_rate | 0.4373 |
| gross_profit_factor | 0.7521 |
| gross_win_rate | 0.4373 |
| sharpe_ratio | -3.9740 |
| sortino_ratio | -1.4176 |
| max_drawdown | 0.7561 |
| cagr | -0.4816 |
| net_avg_win | 48.2805 |
| net_avg_loss | -62.6974 |
| avg_hold_time_bars | 9.7985 |
| exposure | 0.2825 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
