# EMA Hourly Continuation — ALPINE/USDT P21_26

**Symbol:** ALPINE/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1058 |
| net_profit_factor | 0.2647 |
| net_win_rate | 0.3469 |
| gross_profit_factor | 0.6677 |
| gross_win_rate | 0.4093 |
| sharpe_ratio | -13.3940 |
| sortino_ratio | -6.2944 |
| max_drawdown | 0.9998 |
| cagr | -0.9641 |
| net_avg_win | 9.8074 |
| net_avg_loss | -19.6772 |
| avg_hold_time_bars | 3.3819 |
| exposure | 0.1626 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
