# EMA Hourly Continuation — TNSR/USDT P20_144

**Symbol:** TNSR/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 401 |
| net_profit_factor | 0.7688 |
| net_win_rate | 0.4813 |
| gross_profit_factor | 0.9357 |
| gross_win_rate | 0.4813 |
| sharpe_ratio | -1.7702 |
| sortino_ratio | -0.5029 |
| max_drawdown | 0.4760 |
| cagr | -0.2082 |
| net_avg_win | 76.6884 |
| net_avg_loss | -92.5534 |
| avg_hold_time_bars | 29.6359 |
| exposure | 0.5378 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
