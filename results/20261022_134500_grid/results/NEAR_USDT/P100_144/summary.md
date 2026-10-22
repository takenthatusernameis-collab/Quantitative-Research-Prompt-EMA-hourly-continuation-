# EMA Hourly Continuation — NEAR/USDT P100_144

**Symbol:** NEAR/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 480 |
| net_profit_factor | 0.4663 |
| net_win_rate | 0.4688 |
| gross_profit_factor | 0.8327 |
| gross_win_rate | 0.4813 |
| sharpe_ratio | -4.4319 |
| sortino_ratio | -1.3621 |
| max_drawdown | 0.8188 |
| cagr | -0.4880 |
| net_avg_win | 31.6085 |
| net_avg_loss | -59.8065 |
| avg_hold_time_bars | 3.4875 |
| exposure | 0.0761 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
