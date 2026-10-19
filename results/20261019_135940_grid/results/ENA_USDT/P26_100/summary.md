# EMA Hourly Continuation — ENA/USDT P26_100

**Symbol:** ENA/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 642 |
| net_profit_factor | 0.7316 |
| net_win_rate | 0.4953 |
| gross_profit_factor | 0.9901 |
| gross_win_rate | 0.4984 |
| sharpe_ratio | -2.5343 |
| sortino_ratio | -0.9042 |
| max_drawdown | 0.6767 |
| cagr | -0.3500 |
| net_avg_win | 56.6610 |
| net_avg_loss | -76.0125 |
| avg_hold_time_bars | 11.8785 |
| exposure | 0.3466 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
