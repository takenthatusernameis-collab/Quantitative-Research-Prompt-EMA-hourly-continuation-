# EMA Hourly Continuation — AEVO/USDT P26_200

**Symbol:** AEVO/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 353 |
| net_profit_factor | 0.8609 |
| net_win_rate | 0.5269 |
| gross_profit_factor | 1.1163 |
| gross_win_rate | 0.5297 |
| sharpe_ratio | -0.8271 |
| sortino_ratio | -0.2219 |
| max_drawdown | 0.2705 |
| cagr | -0.1004 |
| net_avg_win | 77.9839 |
| net_avg_loss | -100.8853 |
| avg_hold_time_bars | 38.0963 |
| exposure | 0.6085 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
