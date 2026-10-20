# EMA Hourly Continuation — BRETT/USDT P8_144

**Symbol:** BRETT/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 396 |
| net_profit_factor | 0.7434 |
| net_win_rate | 0.4823 |
| gross_profit_factor | 0.9237 |
| gross_win_rate | 0.4848 |
| sharpe_ratio | -1.8258 |
| sortino_ratio | -0.5297 |
| max_drawdown | 0.4597 |
| cagr | -0.2200 |
| net_avg_win | 67.5501 |
| net_avg_loss | -84.6636 |
| avg_hold_time_bars | 41.3687 |
| exposure | 0.7882 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
