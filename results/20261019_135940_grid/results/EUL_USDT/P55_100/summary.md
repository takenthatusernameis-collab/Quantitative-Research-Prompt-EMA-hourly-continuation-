# EMA Hourly Continuation — EUL/USDT P55_100

**Symbol:** EUL/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 542 |
| net_profit_factor | 0.3403 |
| net_win_rate | 0.3967 |
| gross_profit_factor | 0.5961 |
| gross_win_rate | 0.4004 |
| sharpe_ratio | -6.5956 |
| sortino_ratio | -2.1468 |
| max_drawdown | 0.9362 |
| cagr | -0.6633 |
| net_avg_win | 22.4313 |
| net_avg_loss | -43.3426 |
| avg_hold_time_bars | 6.1771 |
| exposure | 0.1522 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
