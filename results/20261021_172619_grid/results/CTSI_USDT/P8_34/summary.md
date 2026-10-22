# EMA Hourly Continuation — CTSI/USDT P8_34

**Symbol:** CTSI/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 813 |
| net_profit_factor | 0.7637 |
| net_win_rate | 0.4920 |
| gross_profit_factor | 1.0339 |
| gross_win_rate | 0.4920 |
| sharpe_ratio | -3.0710 |
| sortino_ratio | -1.2543 |
| max_drawdown | 0.7674 |
| cagr | -0.4366 |
| net_avg_win | 61.6722 |
| net_avg_loss | -78.2135 |
| avg_hold_time_bars | 8.7712 |
| exposure | 0.3241 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
