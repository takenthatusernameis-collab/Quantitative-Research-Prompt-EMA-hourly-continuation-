# EMA Hourly Continuation — AERO/USDT P50_55

**Symbol:** AERO/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 98 |
| net_profit_factor | 0.7246 |
| net_win_rate | 0.4898 |
| gross_profit_factor | 0.9490 |
| gross_win_rate | 0.4898 |
| sharpe_ratio | -0.9635 |
| sortino_ratio | -0.1366 |
| max_drawdown | 0.1753 |
| cagr | -0.0608 |
| net_avg_win | 79.9277 |
| net_avg_loss | -105.8905 |
| avg_hold_time_bars | 5.2347 |
| exposure | 0.0233 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
