# EMA Hourly Continuation — VELO/USDT P21_26

**Symbol:** VELO/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1248 |
| net_profit_factor | 0.3694 |
| net_win_rate | 0.3622 |
| gross_profit_factor | 0.7389 |
| gross_win_rate | 0.3998 |
| sharpe_ratio | -13.5234 |
| sortino_ratio | -6.8475 |
| max_drawdown | 0.9999 |
| cagr | -0.9725 |
| net_avg_win | 12.9564 |
| net_avg_loss | -19.9184 |
| avg_hold_time_bars | 1.8526 |
| exposure | 0.1051 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
