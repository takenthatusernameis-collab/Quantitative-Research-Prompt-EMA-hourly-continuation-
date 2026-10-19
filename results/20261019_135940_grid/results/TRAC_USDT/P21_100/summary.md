# EMA Hourly Continuation — TRAC/USDT P21_100

**Symbol:** TRAC/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 691 |
| net_profit_factor | 0.6910 |
| net_win_rate | 0.4949 |
| gross_profit_factor | 1.0158 |
| gross_win_rate | 0.4993 |
| sharpe_ratio | -3.1730 |
| sortino_ratio | -1.1713 |
| max_drawdown | 0.7684 |
| cagr | -0.4307 |
| net_avg_win | 49.5031 |
| net_avg_loss | -70.2025 |
| avg_hold_time_bars | 11.7192 |
| exposure | 0.3681 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
