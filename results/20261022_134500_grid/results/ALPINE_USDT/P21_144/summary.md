# EMA Hourly Continuation — ALPINE/USDT P21_144

**Symbol:** ALPINE/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 274 |
| net_profit_factor | 0.7582 |
| net_win_rate | 0.5073 |
| gross_profit_factor | 1.0233 |
| gross_win_rate | 0.5073 |
| sharpe_ratio | -1.3471 |
| sortino_ratio | -0.3162 |
| max_drawdown | 0.3597 |
| cagr | -0.1372 |
| net_avg_win | 69.8863 |
| net_avg_loss | -94.8992 |
| avg_hold_time_bars | 59.3540 |
| exposure | 0.7392 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
