# EMA Hourly Continuation — SUN/USDT P50_200

**Symbol:** SUN/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 281 |
| net_profit_factor | 0.6083 |
| net_win_rate | 0.4591 |
| gross_profit_factor | 0.9059 |
| gross_win_rate | 0.4591 |
| sharpe_ratio | -2.9776 |
| sortino_ratio | -0.7061 |
| max_drawdown | 0.5786 |
| cagr | -0.2822 |
| net_avg_win | 68.2284 |
| net_avg_loss | -95.1927 |
| avg_hold_time_bars | 32.2456 |
| exposure | 0.4100 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
