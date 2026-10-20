# EMA Hourly Continuation — PROM/USDT P100_144

**Symbol:** PROM/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 584 |
| net_profit_factor | 0.2999 |
| net_win_rate | 0.3647 |
| gross_profit_factor | 0.6485 |
| gross_win_rate | 0.4041 |
| sharpe_ratio | -8.5762 |
| sortino_ratio | -2.9515 |
| max_drawdown | 0.9780 |
| cagr | -0.7788 |
| net_avg_win | 19.6573 |
| net_avg_loss | -37.6303 |
| avg_hold_time_bars | 4.3134 |
| exposure | 0.1145 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
