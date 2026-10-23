# EMA Hourly Continuation — CKB/USDT P8_20

**Symbol:** CKB/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1668 |
| net_profit_factor | 0.3840 |
| net_win_rate | 0.4137 |
| gross_profit_factor | 0.7783 |
| gross_win_rate | 0.4412 |
| sharpe_ratio | -12.6200 |
| sortino_ratio | -7.2607 |
| max_drawdown | 0.9999 |
| cagr | -0.9749 |
| net_avg_win | 9.0331 |
| net_avg_loss | -16.5970 |
| avg_hold_time_bars | 3.0647 |
| exposure | 0.2324 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
