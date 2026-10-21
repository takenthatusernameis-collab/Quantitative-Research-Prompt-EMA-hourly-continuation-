# EMA Hourly Continuation — THETA/USDT P50_144

**Symbol:** THETA/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 342 |
| net_profit_factor | 0.8267 |
| net_win_rate | 0.5117 |
| gross_profit_factor | 1.0385 |
| gross_win_rate | 0.5117 |
| sharpe_ratio | -1.0631 |
| sortino_ratio | -0.2824 |
| max_drawdown | 0.3130 |
| cagr | -0.1233 |
| net_avg_win | 76.6648 |
| net_avg_loss | -97.1840 |
| avg_hold_time_bars | 15.9415 |
| exposure | 0.2478 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
