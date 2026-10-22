# EMA Hourly Continuation — ETN/USDT P20_34

**Symbol:** ETN/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 279 |
| net_profit_factor | 0.3938 |
| net_win_rate | 0.3441 |
| gross_profit_factor | 0.5232 |
| gross_win_rate | 0.3441 |
| sharpe_ratio | -5.2442 |
| sortino_ratio | -1.3534 |
| max_drawdown | 0.7413 |
| cagr | -0.4697 |
| net_avg_win | 49.8304 |
| net_avg_loss | -66.3773 |
| avg_hold_time_bars | 6.4444 |
| exposure | 0.0977 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
