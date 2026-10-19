# EMA Hourly Continuation — SHIB/USDT P50_55

**Symbol:** SHIB/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 814 |
| net_profit_factor | 0.2086 |
| net_win_rate | 0.2948 |
| gross_profit_factor | 0.7863 |
| gross_win_rate | 0.3747 |
| sharpe_ratio | -14.6626 |
| sortino_ratio | -6.4060 |
| max_drawdown | 0.9999 |
| cagr | -0.9723 |
| net_avg_win | 10.9845 |
| net_avg_loss | -22.0123 |
| avg_hold_time_bars | 1.8931 |
| exposure | 0.0700 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
