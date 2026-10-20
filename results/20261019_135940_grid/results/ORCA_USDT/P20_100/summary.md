# EMA Hourly Continuation — ORCA/USDT P20_100

**Symbol:** ORCA/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 611 |
| net_profit_factor | 0.6475 |
| net_win_rate | 0.4861 |
| gross_profit_factor | 0.9540 |
| gross_win_rate | 0.4992 |
| sharpe_ratio | -3.2219 |
| sortino_ratio | -1.1228 |
| max_drawdown | 0.7648 |
| cagr | -0.4139 |
| net_avg_win | 45.6792 |
| net_avg_loss | -66.7282 |
| avg_hold_time_bars | 16.2226 |
| exposure | 0.4505 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
