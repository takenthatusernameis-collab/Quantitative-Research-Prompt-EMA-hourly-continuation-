# EMA Hourly Continuation — GMEE/USDT P21_144

**Symbol:** GMEE/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 466 |
| net_profit_factor | 0.5630 |
| net_win_rate | 0.4292 |
| gross_profit_factor | 0.7791 |
| gross_win_rate | 0.4378 |
| sharpe_ratio | -3.9522 |
| sortino_ratio | -1.1875 |
| max_drawdown | 0.7757 |
| cagr | -0.4399 |
| net_avg_win | 49.3860 |
| net_avg_loss | -65.9577 |
| avg_hold_time_bars | 26.4614 |
| exposure | 0.5605 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
