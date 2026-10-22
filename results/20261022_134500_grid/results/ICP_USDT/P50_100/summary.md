# EMA Hourly Continuation — ICP/USDT P50_100

**Symbol:** ICP/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 664 |
| net_profit_factor | 0.5312 |
| net_win_rate | 0.4759 |
| gross_profit_factor | 0.9219 |
| gross_win_rate | 0.4819 |
| sharpe_ratio | -5.0918 |
| sortino_ratio | -1.8471 |
| max_drawdown | 0.8978 |
| cagr | -0.5926 |
| net_avg_win | 32.0963 |
| net_avg_loss | -54.8674 |
| avg_hold_time_bars | 5.4955 |
| exposure | 0.1659 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
