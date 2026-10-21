# EMA Hourly Continuation — VELO/USDT P34_144

**Symbol:** VELO/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 391 |
| net_profit_factor | 0.8804 |
| net_win_rate | 0.5115 |
| gross_profit_factor | 1.0292 |
| gross_win_rate | 0.5115 |
| sharpe_ratio | -0.7106 |
| sortino_ratio | -0.2015 |
| max_drawdown | 0.2873 |
| cagr | -0.0920 |
| net_avg_win | 79.2437 |
| net_avg_loss | -94.2486 |
| avg_hold_time_bars | 20.2225 |
| exposure | 0.3594 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
