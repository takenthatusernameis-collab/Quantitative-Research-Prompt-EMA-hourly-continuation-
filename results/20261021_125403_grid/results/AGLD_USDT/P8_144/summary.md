# EMA Hourly Continuation — AGLD/USDT P8_144

**Symbol:** AGLD/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 406 |
| net_profit_factor | 0.8279 |
| net_win_rate | 0.4926 |
| gross_profit_factor | 0.9808 |
| gross_win_rate | 0.4926 |
| sharpe_ratio | -1.2673 |
| sortino_ratio | -0.3639 |
| max_drawdown | 0.4376 |
| cagr | -0.1557 |
| net_avg_win | 83.5921 |
| net_avg_loss | -98.0222 |
| avg_hold_time_bars | 39.1207 |
| exposure | 0.7188 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
