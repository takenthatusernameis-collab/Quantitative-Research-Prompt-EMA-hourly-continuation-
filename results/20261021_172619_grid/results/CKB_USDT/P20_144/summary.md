# EMA Hourly Continuation — CKB/USDT P20_144

**Symbol:** CKB/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 410 |
| net_profit_factor | 0.7813 |
| net_win_rate | 0.4951 |
| gross_profit_factor | 0.9628 |
| gross_win_rate | 0.4951 |
| sharpe_ratio | -1.5112 |
| sortino_ratio | -0.4373 |
| max_drawdown | 0.4146 |
| cagr | -0.1836 |
| net_avg_win | 70.2442 |
| net_avg_loss | -88.1663 |
| avg_hold_time_bars | 27.4512 |
| exposure | 0.5116 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
