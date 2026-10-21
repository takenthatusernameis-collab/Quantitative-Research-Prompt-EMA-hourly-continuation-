# EMA Hourly Continuation — AGLD/USDT P21_144

**Symbol:** AGLD/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 457 |
| net_profit_factor | 0.7824 |
| net_win_rate | 0.4792 |
| gross_profit_factor | 0.9531 |
| gross_win_rate | 0.4792 |
| sharpe_ratio | -1.9276 |
| sortino_ratio | -0.5858 |
| max_drawdown | 0.5717 |
| cagr | -0.2366 |
| net_avg_win | 81.1047 |
| net_avg_loss | -95.3808 |
| avg_hold_time_bars | 25.0591 |
| exposure | 0.5183 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
