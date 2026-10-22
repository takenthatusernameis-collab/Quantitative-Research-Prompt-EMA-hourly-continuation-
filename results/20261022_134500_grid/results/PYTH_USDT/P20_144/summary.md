# EMA Hourly Continuation — PYTH/USDT P20_144

**Symbol:** PYTH/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 503 |
| net_profit_factor | 0.7456 |
| net_win_rate | 0.4950 |
| gross_profit_factor | 1.0056 |
| gross_win_rate | 0.4970 |
| sharpe_ratio | -2.1516 |
| sortino_ratio | -0.6847 |
| max_drawdown | 0.5785 |
| cagr | -0.2741 |
| net_avg_win | 65.0604 |
| net_avg_loss | -85.5398 |
| avg_hold_time_bars | 24.1133 |
| exposure | 0.5513 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
