# EMA Hourly Continuation — PYTH/USDT P55_144

**Symbol:** PYTH/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 517 |
| net_profit_factor | 0.6023 |
| net_win_rate | 0.4778 |
| gross_profit_factor | 0.9130 |
| gross_win_rate | 0.4836 |
| sharpe_ratio | -3.3213 |
| sortino_ratio | -1.0636 |
| max_drawdown | 0.7341 |
| cagr | -0.3987 |
| net_avg_win | 44.2122 |
| net_avg_loss | -67.1575 |
| avg_hold_time_bars | 10.1335 |
| exposure | 0.2381 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
