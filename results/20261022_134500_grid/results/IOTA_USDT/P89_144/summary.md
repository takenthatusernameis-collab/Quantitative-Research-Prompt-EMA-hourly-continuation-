# EMA Hourly Continuation — IOTA/USDT P89_144

**Symbol:** IOTA/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 467 |
| net_profit_factor | 0.5504 |
| net_win_rate | 0.4732 |
| gross_profit_factor | 1.0213 |
| gross_win_rate | 0.4925 |
| sharpe_ratio | -4.1905 |
| sortino_ratio | -1.2748 |
| max_drawdown | 0.8023 |
| cagr | -0.4635 |
| net_avg_win | 43.7992 |
| net_avg_loss | -71.4875 |
| avg_hold_time_bars | 5.4882 |
| exposure | 0.1165 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
