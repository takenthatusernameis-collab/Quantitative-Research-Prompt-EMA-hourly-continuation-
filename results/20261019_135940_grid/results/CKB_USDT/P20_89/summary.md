# EMA Hourly Continuation — CKB/USDT P20_89

**Symbol:** CKB/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 763 |
| net_profit_factor | 0.6031 |
| net_win_rate | 0.4548 |
| gross_profit_factor | 0.9045 |
| gross_win_rate | 0.4679 |
| sharpe_ratio | -5.1296 |
| sortino_ratio | -1.9924 |
| max_drawdown | 0.9120 |
| cagr | -0.6182 |
| net_avg_win | 39.8849 |
| net_avg_loss | -55.1658 |
| avg_hold_time_bars | 10.8965 |
| exposure | 0.3779 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
