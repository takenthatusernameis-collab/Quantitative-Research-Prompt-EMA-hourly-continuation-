# EMA Hourly Continuation — DEGEN/USDT P100_144

**Symbol:** DEGEN/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 217 |
| net_profit_factor | 0.8734 |
| net_win_rate | 0.5253 |
| gross_profit_factor | 1.1051 |
| gross_win_rate | 0.5253 |
| sharpe_ratio | -0.6287 |
| sortino_ratio | -0.1335 |
| max_drawdown | 0.2250 |
| cagr | -0.0614 |
| net_avg_win | 88.9296 |
| net_avg_loss | -112.6916 |
| avg_hold_time_bars | 8.2396 |
| exposure | 0.0814 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
