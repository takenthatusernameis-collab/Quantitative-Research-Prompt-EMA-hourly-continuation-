# EMA Hourly Continuation — QI/USDT P12_100

**Symbol:** QI/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 478 |
| net_profit_factor | 0.7968 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9980 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.5681 |
| sortino_ratio | -0.4897 |
| max_drawdown | 0.4821 |
| cagr | -0.2024 |
| net_avg_win | 71.3383 |
| net_avg_loss | -89.5307 |
| avg_hold_time_bars | 25.9519 |
| exposure | 0.5613 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
