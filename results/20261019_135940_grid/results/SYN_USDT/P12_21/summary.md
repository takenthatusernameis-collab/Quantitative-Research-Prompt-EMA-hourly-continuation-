# EMA Hourly Continuation — SYN/USDT P12_21

**Symbol:** SYN/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1422 |
| net_profit_factor | 0.3719 |
| net_win_rate | 0.4058 |
| gross_profit_factor | 0.7552 |
| gross_win_rate | 0.4297 |
| sharpe_ratio | -11.3595 |
| sortino_ratio | -6.0485 |
| max_drawdown | 0.9995 |
| cagr | -0.9522 |
| net_avg_win | 10.2562 |
| net_avg_loss | -18.8320 |
| avg_hold_time_bars | 2.7426 |
| exposure | 0.1773 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
