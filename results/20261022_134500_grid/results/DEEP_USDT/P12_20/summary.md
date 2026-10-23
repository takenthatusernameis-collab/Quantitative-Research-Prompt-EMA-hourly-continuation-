# EMA Hourly Continuation — DEEP/USDT P12_20

**Symbol:** DEEP/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1115 |
| net_profit_factor | 0.5291 |
| net_win_rate | 0.4278 |
| gross_profit_factor | 0.8909 |
| gross_win_rate | 0.4493 |
| sharpe_ratio | -10.5297 |
| sortino_ratio | -5.5269 |
| max_drawdown | 0.9966 |
| cagr | -0.9398 |
| net_avg_win | 23.4694 |
| net_avg_loss | -33.1665 |
| avg_hold_time_bars | 2.2224 |
| exposure | 0.1403 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
