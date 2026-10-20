# EMA Hourly Continuation — SATS/USDT P55_89

**Symbol:** SATS/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 582 |
| net_profit_factor | 0.4844 |
| net_win_rate | 0.4450 |
| gross_profit_factor | 0.8030 |
| gross_win_rate | 0.4536 |
| sharpe_ratio | -5.0599 |
| sortino_ratio | -1.7119 |
| max_drawdown | 0.8793 |
| cagr | -0.5641 |
| net_avg_win | 31.8108 |
| net_avg_loss | -52.6551 |
| avg_hold_time_bars | 5.1546 |
| exposure | 0.1358 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
