# EMA Hourly Continuation — ZETA/USDT P12_55

**Symbol:** ZETA/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 647 |
| net_profit_factor | 0.7619 |
| net_win_rate | 0.4853 |
| gross_profit_factor | 0.9734 |
| gross_win_rate | 0.4853 |
| sharpe_ratio | -2.5397 |
| sortino_ratio | -0.9207 |
| max_drawdown | 0.6738 |
| cagr | -0.3449 |
| net_avg_win | 66.8473 |
| net_avg_loss | -82.7306 |
| avg_hold_time_bars | 13.1499 |
| exposure | 0.3850 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
