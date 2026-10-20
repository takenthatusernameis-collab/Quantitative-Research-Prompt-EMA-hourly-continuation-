# EMA Hourly Continuation — DYDX/USDT P21_50

**Symbol:** DYDX/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1006 |
| net_profit_factor | 0.5253 |
| net_win_rate | 0.4443 |
| gross_profit_factor | 0.9362 |
| gross_win_rate | 0.4583 |
| sharpe_ratio | -7.4003 |
| sortino_ratio | -3.2844 |
| max_drawdown | 0.9838 |
| cagr | -0.8031 |
| net_avg_win | 24.3426 |
| net_avg_loss | -37.0523 |
| avg_hold_time_bars | 4.5527 |
| exposure | 0.2082 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
