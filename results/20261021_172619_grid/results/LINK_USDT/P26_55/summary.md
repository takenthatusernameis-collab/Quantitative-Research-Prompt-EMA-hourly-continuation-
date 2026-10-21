# EMA Hourly Continuation — LINK/USDT P26_55

**Symbol:** LINK/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 403 |
| net_profit_factor | 0.6995 |
| net_win_rate | 0.4888 |
| gross_profit_factor | 0.9649 |
| gross_win_rate | 0.4888 |
| sharpe_ratio | -2.3312 |
| sortino_ratio | -0.6706 |
| max_drawdown | 0.5525 |
| cagr | -0.2642 |
| net_avg_win | 63.4891 |
| net_avg_loss | -86.7964 |
| avg_hold_time_bars | 7.3251 |
| exposure | 0.1342 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
