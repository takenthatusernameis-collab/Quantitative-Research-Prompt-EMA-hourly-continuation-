# EMA Hourly Continuation — DYDX/USDT P12_26

**Symbol:** DYDX/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 462 |
| net_profit_factor | 0.6960 |
| net_win_rate | 0.4719 |
| gross_profit_factor | 0.9435 |
| gross_win_rate | 0.4719 |
| sharpe_ratio | -2.8091 |
| sortino_ratio | -0.8624 |
| max_drawdown | 0.6358 |
| cagr | -0.3258 |
| net_avg_win | 66.0016 |
| net_avg_loss | -84.7225 |
| avg_hold_time_bars | 5.6883 |
| exposure | 0.1195 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
