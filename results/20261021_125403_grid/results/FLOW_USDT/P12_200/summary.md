# EMA Hourly Continuation — FLOW/USDT P12_200

**Symbol:** FLOW/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 271 |
| net_profit_factor | 0.7729 |
| net_win_rate | 0.4797 |
| gross_profit_factor | 0.9173 |
| gross_win_rate | 0.4797 |
| sharpe_ratio | -1.3284 |
| sortino_ratio | -0.3110 |
| max_drawdown | 0.3263 |
| cagr | -0.1346 |
| net_avg_win | 79.7044 |
| net_avg_loss | -95.0838 |
| avg_hold_time_bars | 61.2030 |
| exposure | 0.7539 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
