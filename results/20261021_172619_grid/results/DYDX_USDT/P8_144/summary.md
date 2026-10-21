# EMA Hourly Continuation — DYDX/USDT P8_144

**Symbol:** DYDX/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 324 |
| net_profit_factor | 0.9657 |
| net_win_rate | 0.5340 |
| gross_profit_factor | 1.1283 |
| gross_win_rate | 0.5340 |
| sharpe_ratio | -0.1419 |
| sortino_ratio | -0.0368 |
| max_drawdown | 0.1213 |
| cagr | -0.0223 |
| net_avg_win | 89.2979 |
| net_avg_loss | -105.9467 |
| avg_hold_time_bars | 51.7685 |
| exposure | 0.7624 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
