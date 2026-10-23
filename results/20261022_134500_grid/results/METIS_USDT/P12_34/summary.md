# EMA Hourly Continuation — METIS/USDT P12_34

**Symbol:** METIS/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1309 |
| net_profit_factor | 0.4570 |
| net_win_rate | 0.4309 |
| gross_profit_factor | 0.8422 |
| gross_win_rate | 0.4461 |
| sharpe_ratio | -9.1650 |
| sortino_ratio | -4.6558 |
| max_drawdown | 0.9969 |
| cagr | -0.8993 |
| net_avg_win | 14.8769 |
| net_avg_loss | -24.6432 |
| avg_hold_time_bars | 4.3613 |
| exposure | 0.2595 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
