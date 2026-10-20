# EMA Hourly Continuation — DEXE/USDT P89_100

**Symbol:** DEXE/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 510 |
| net_profit_factor | 0.2427 |
| net_win_rate | 0.3686 |
| gross_profit_factor | 0.6433 |
| gross_win_rate | 0.3941 |
| sharpe_ratio | -8.6910 |
| sortino_ratio | -2.8179 |
| max_drawdown | 0.9776 |
| cagr | -0.7791 |
| net_avg_win | 16.6605 |
| net_avg_loss | -40.0830 |
| avg_hold_time_bars | 6.2824 |
| exposure | 0.1456 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
