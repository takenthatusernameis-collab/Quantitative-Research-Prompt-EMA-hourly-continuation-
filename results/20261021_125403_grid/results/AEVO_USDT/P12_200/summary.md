# EMA Hourly Continuation — AEVO/USDT P12_200

**Symbol:** AEVO/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 243 |
| net_profit_factor | 0.9307 |
| net_win_rate | 0.5185 |
| gross_profit_factor | 1.0748 |
| gross_win_rate | 0.5185 |
| sharpe_ratio | -0.3207 |
| sortino_ratio | -0.0718 |
| max_drawdown | 0.2302 |
| cagr | -0.0357 |
| net_avg_win | 93.3252 |
| net_avg_loss | -107.9869 |
| avg_hold_time_bars | 70.1481 |
| exposure | 0.7713 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
