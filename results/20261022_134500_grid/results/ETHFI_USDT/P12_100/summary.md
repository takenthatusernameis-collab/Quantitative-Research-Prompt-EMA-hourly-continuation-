# EMA Hourly Continuation — ETHFI/USDT P12_100

**Symbol:** ETHFI/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 667 |
| net_profit_factor | 0.6610 |
| net_win_rate | 0.4663 |
| gross_profit_factor | 0.9211 |
| gross_win_rate | 0.4723 |
| sharpe_ratio | -3.6781 |
| sortino_ratio | -1.3341 |
| max_drawdown | 0.8004 |
| cagr | -0.4705 |
| net_avg_win | 49.9919 |
| net_avg_loss | -66.0715 |
| avg_hold_time_bars | 18.9415 |
| exposure | 0.5743 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
