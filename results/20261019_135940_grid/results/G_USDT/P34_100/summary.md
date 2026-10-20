# EMA Hourly Continuation — G/USDT P34_100

**Symbol:** G/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 525 |
| net_profit_factor | 0.5249 |
| net_win_rate | 0.4495 |
| gross_profit_factor | 0.8671 |
| gross_win_rate | 0.4686 |
| sharpe_ratio | -4.7111 |
| sortino_ratio | -1.6365 |
| max_drawdown | 0.8285 |
| cagr | -0.5413 |
| net_avg_win | 38.1835 |
| net_avg_loss | -59.4090 |
| avg_hold_time_bars | 11.3600 |
| exposure | 0.3136 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
