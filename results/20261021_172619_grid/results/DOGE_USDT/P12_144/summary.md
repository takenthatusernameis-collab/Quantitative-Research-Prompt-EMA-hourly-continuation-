# EMA Hourly Continuation — DOGE/USDT P12_144

**Symbol:** DOGE/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 374 |
| net_profit_factor | 0.7297 |
| net_win_rate | 0.4813 |
| gross_profit_factor | 0.9231 |
| gross_win_rate | 0.4813 |
| sharpe_ratio | -1.9231 |
| sortino_ratio | -0.5300 |
| max_drawdown | 0.4944 |
| cagr | -0.2167 |
| net_avg_win | 68.7651 |
| net_avg_loss | -87.4347 |
| avg_hold_time_bars | 37.9171 |
| exposure | 0.6446 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
