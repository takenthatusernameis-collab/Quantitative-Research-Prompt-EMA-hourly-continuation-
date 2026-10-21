# EMA Hourly Continuation — DYDX/USDT P34_89

**Symbol:** DYDX/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 439 |
| net_profit_factor | 0.7253 |
| net_win_rate | 0.4806 |
| gross_profit_factor | 0.9260 |
| gross_win_rate | 0.4806 |
| sharpe_ratio | -2.1108 |
| sortino_ratio | -0.6307 |
| max_drawdown | 0.5518 |
| cagr | -0.2510 |
| net_avg_win | 64.5774 |
| net_avg_loss | -82.3973 |
| avg_hold_time_bars | 10.6560 |
| exposure | 0.2126 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
