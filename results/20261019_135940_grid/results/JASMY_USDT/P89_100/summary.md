# EMA Hourly Continuation — JASMY/USDT P89_100

**Symbol:** JASMY/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 601 |
| net_profit_factor | 0.3450 |
| net_win_rate | 0.4309 |
| gross_profit_factor | 0.8471 |
| gross_win_rate | 0.4559 |
| sharpe_ratio | -8.2232 |
| sortino_ratio | -2.8870 |
| max_drawdown | 0.9788 |
| cagr | -0.7822 |
| net_avg_win | 19.8957 |
| net_avg_loss | -43.6704 |
| avg_hold_time_bars | 2.1098 |
| exposure | 0.0576 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
