# EMA Hourly Continuation — OP/USDT P50_100

**Symbol:** OP/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 378 |
| net_profit_factor | 0.7806 |
| net_win_rate | 0.5026 |
| gross_profit_factor | 1.0140 |
| gross_win_rate | 0.5026 |
| sharpe_ratio | -1.5297 |
| sortino_ratio | -0.4268 |
| max_drawdown | 0.4197 |
| cagr | -0.1784 |
| net_avg_win | 72.9656 |
| net_avg_loss | -94.4624 |
| avg_hold_time_bars | 7.9868 |
| exposure | 0.1372 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
