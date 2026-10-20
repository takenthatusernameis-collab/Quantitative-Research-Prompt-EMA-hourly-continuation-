# EMA Hourly Continuation — CKB/USDT P26_100

**Symbol:** CKB/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 648 |
| net_profit_factor | 0.5795 |
| net_win_rate | 0.4537 |
| gross_profit_factor | 0.8908 |
| gross_win_rate | 0.4645 |
| sharpe_ratio | -4.9912 |
| sortino_ratio | -1.7819 |
| max_drawdown | 0.8924 |
| cagr | -0.5824 |
| net_avg_win | 41.6434 |
| net_avg_loss | -59.6810 |
| avg_hold_time_bars | 12.5046 |
| exposure | 0.3683 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
