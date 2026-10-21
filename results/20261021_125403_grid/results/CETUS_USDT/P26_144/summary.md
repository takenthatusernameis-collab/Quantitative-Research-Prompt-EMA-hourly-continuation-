# EMA Hourly Continuation — CETUS/USDT P26_144

**Symbol:** CETUS/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 355 |
| net_profit_factor | 0.9436 |
| net_win_rate | 0.5296 |
| gross_profit_factor | 1.1215 |
| gross_win_rate | 0.5296 |
| sharpe_ratio | -0.3289 |
| sortino_ratio | -0.0891 |
| max_drawdown | 0.2789 |
| cagr | -0.0453 |
| net_avg_win | 98.2317 |
| net_avg_loss | -117.1926 |
| avg_hold_time_bars | 30.5803 |
| exposure | 0.4913 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
