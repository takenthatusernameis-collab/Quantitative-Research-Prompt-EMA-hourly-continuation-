# EMA Hourly Continuation — SYN/USDT P26_34

**Symbol:** SYN/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 281 |
| net_profit_factor | 0.6434 |
| net_win_rate | 0.4698 |
| gross_profit_factor | 0.9032 |
| gross_win_rate | 0.4698 |
| sharpe_ratio | -2.4126 |
| sortino_ratio | -0.5785 |
| max_drawdown | 0.4998 |
| cagr | -0.2329 |
| net_avg_win | 66.4481 |
| net_avg_loss | -91.4898 |
| avg_hold_time_bars | 4.7758 |
| exposure | 0.0610 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
