# EMA Hourly Continuation — COMP/USDT P8_12

**Symbol:** COMP/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 378 |
| net_profit_factor | 0.5986 |
| net_win_rate | 0.4841 |
| gross_profit_factor | 0.9568 |
| gross_win_rate | 0.4841 |
| sharpe_ratio | -3.3009 |
| sortino_ratio | -0.9248 |
| max_drawdown | 0.6853 |
| cagr | -0.3461 |
| net_avg_win | 53.4477 |
| net_avg_loss | -83.7910 |
| avg_hold_time_bars | 4.2540 |
| exposure | 0.0731 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
