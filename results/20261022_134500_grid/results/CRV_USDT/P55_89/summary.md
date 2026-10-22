# EMA Hourly Continuation — CRV/USDT P55_89

**Symbol:** CRV/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 719 |
| net_profit_factor | 0.4747 |
| net_win_rate | 0.4534 |
| gross_profit_factor | 0.8473 |
| gross_win_rate | 0.4645 |
| sharpe_ratio | -6.1570 |
| sortino_ratio | -2.3418 |
| max_drawdown | 0.9441 |
| cagr | -0.6792 |
| net_avg_win | 26.1254 |
| net_avg_loss | -45.6519 |
| avg_hold_time_bars | 3.4451 |
| exposure | 0.1126 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
