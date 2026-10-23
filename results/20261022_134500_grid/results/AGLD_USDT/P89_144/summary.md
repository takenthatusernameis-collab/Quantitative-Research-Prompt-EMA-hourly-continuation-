# EMA Hourly Continuation — AGLD/USDT P89_144

**Symbol:** AGLD/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 499 |
| net_profit_factor | 0.6098 |
| net_win_rate | 0.4649 |
| gross_profit_factor | 0.9755 |
| gross_win_rate | 0.4749 |
| sharpe_ratio | -3.9581 |
| sortino_ratio | -1.2480 |
| max_drawdown | 0.7763 |
| cagr | -0.4447 |
| net_avg_win | 52.0806 |
| net_avg_loss | -74.2123 |
| avg_hold_time_bars | 6.3327 |
| exposure | 0.1430 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
