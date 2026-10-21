# EMA Hourly Continuation — CKB/USDT P21_50

**Symbol:** CKB/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 516 |
| net_profit_factor | 0.6487 |
| net_win_rate | 0.4651 |
| gross_profit_factor | 0.8648 |
| gross_win_rate | 0.4651 |
| sharpe_ratio | -3.2115 |
| sortino_ratio | -1.0404 |
| max_drawdown | 0.7075 |
| cagr | -0.3787 |
| net_avg_win | 53.6600 |
| net_avg_loss | -71.9256 |
| avg_hold_time_bars | 6.9942 |
| exposure | 0.1640 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
