# EMA Hourly Continuation — CETUS/USDT P100_144

**Symbol:** CETUS/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 461 |
| net_profit_factor | 0.5610 |
| net_win_rate | 0.4577 |
| gross_profit_factor | 0.9562 |
| gross_win_rate | 0.4751 |
| sharpe_ratio | -4.4889 |
| sortino_ratio | -1.3483 |
| max_drawdown | 0.8165 |
| cagr | -0.4860 |
| net_avg_win | 49.2568 |
| net_avg_loss | -74.1070 |
| avg_hold_time_bars | 3.9935 |
| exposure | 0.0833 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
