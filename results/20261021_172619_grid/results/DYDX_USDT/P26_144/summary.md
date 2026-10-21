# EMA Hourly Continuation — DYDX/USDT P26_144

**Symbol:** DYDX/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 344 |
| net_profit_factor | 1.0104 |
| net_win_rate | 0.5494 |
| gross_profit_factor | 1.2004 |
| gross_win_rate | 0.5494 |
| sharpe_ratio | 0.1218 |
| sortino_ratio | 0.0328 |
| max_drawdown | 0.1773 |
| cagr | 0.0074 |
| net_avg_win | 96.1640 |
| net_avg_loss | -116.0469 |
| avg_hold_time_bars | 31.1919 |
| exposure | 0.4877 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
