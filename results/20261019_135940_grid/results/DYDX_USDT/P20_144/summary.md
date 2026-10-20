# EMA Hourly Continuation — DYDX/USDT P20_144

**Symbol:** DYDX/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 469 |
| net_profit_factor | 0.7031 |
| net_win_rate | 0.4904 |
| gross_profit_factor | 0.9952 |
| gross_win_rate | 0.4968 |
| sharpe_ratio | -2.4426 |
| sortino_ratio | -0.7488 |
| max_drawdown | 0.5961 |
| cagr | -0.2952 |
| net_avg_win | 60.1828 |
| net_avg_loss | -82.3765 |
| avg_hold_time_bars | 27.2601 |
| exposure | 0.5811 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
