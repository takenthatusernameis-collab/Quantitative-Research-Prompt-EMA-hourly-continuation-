# EMA Hourly Continuation — CKB/USDT P8_20

**Symbol:** CKB/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 623 |
| net_profit_factor | 0.6593 |
| net_win_rate | 0.4767 |
| gross_profit_factor | 0.9232 |
| gross_win_rate | 0.4767 |
| sharpe_ratio | -3.5692 |
| sortino_ratio | -1.2756 |
| max_drawdown | 0.7802 |
| cagr | -0.4419 |
| net_avg_win | 50.1044 |
| net_avg_loss | -69.2308 |
| avg_hold_time_bars | 5.2231 |
| exposure | 0.1479 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
