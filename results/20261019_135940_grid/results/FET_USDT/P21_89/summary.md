# EMA Hourly Continuation — FET/USDT P21_89

**Symbol:** FET/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 678 |
| net_profit_factor | 0.6413 |
| net_win_rate | 0.4749 |
| gross_profit_factor | 0.9232 |
| gross_win_rate | 0.4808 |
| sharpe_ratio | -3.7658 |
| sortino_ratio | -1.3799 |
| max_drawdown | 0.8208 |
| cagr | -0.4813 |
| net_avg_win | 44.8362 |
| net_avg_loss | -63.2416 |
| avg_hold_time_bars | 12.7640 |
| exposure | 0.3934 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
