# EMA Hourly Continuation — OSMO/USDT P26_200

**Symbol:** OSMO/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 387 |
| net_profit_factor | 0.7549 |
| net_win_rate | 0.5039 |
| gross_profit_factor | 1.0503 |
| gross_win_rate | 0.5116 |
| sharpe_ratio | -1.7531 |
| sortino_ratio | -0.4892 |
| max_drawdown | 0.4549 |
| cagr | -0.2073 |
| net_avg_win | 69.8040 |
| net_avg_loss | -93.9120 |
| avg_hold_time_bars | 32.1189 |
| exposure | 0.5650 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
