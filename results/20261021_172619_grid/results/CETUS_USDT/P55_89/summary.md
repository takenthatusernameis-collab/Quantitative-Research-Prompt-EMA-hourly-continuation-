# EMA Hourly Continuation — CETUS/USDT P55_89

**Symbol:** CETUS/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 380 |
| net_profit_factor | 0.6665 |
| net_win_rate | 0.4658 |
| gross_profit_factor | 0.8758 |
| gross_win_rate | 0.4658 |
| sharpe_ratio | -2.5472 |
| sortino_ratio | -0.7062 |
| max_drawdown | 0.5594 |
| cagr | -0.2774 |
| net_avg_win | 63.1533 |
| net_avg_loss | -82.6204 |
| avg_hold_time_bars | 6.2763 |
| exposure | 0.1079 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
