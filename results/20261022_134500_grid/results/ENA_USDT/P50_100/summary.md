# EMA Hourly Continuation — ENA/USDT P50_100

**Symbol:** ENA/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 566 |
| net_profit_factor | 0.6313 |
| net_win_rate | 0.4788 |
| gross_profit_factor | 0.9158 |
| gross_win_rate | 0.4806 |
| sharpe_ratio | -3.5022 |
| sortino_ratio | -1.1724 |
| max_drawdown | 0.7631 |
| cagr | -0.4282 |
| net_avg_win | 47.6654 |
| net_avg_loss | -69.3566 |
| avg_hold_time_bars | 6.2986 |
| exposure | 0.1620 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
