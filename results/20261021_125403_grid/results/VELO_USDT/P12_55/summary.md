# EMA Hourly Continuation — VELO/USDT P12_55

**Symbol:** VELO/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 642 |
| net_profit_factor | 0.8435 |
| net_win_rate | 0.5140 |
| gross_profit_factor | 1.0211 |
| gross_win_rate | 0.5140 |
| sharpe_ratio | -1.1274 |
| sortino_ratio | -0.4103 |
| max_drawdown | 0.4737 |
| cagr | -0.1756 |
| net_avg_win | 62.7498 |
| net_avg_loss | -78.6854 |
| avg_hold_time_bars | 10.4424 |
| exposure | 0.3047 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
