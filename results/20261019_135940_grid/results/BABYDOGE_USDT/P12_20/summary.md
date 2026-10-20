# EMA Hourly Continuation — BABYDOGE/USDT P12_20

**Symbol:** BABYDOGE/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 18 |
| net_profit_factor | 0.8956 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9883 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -0.1320 |
| sortino_ratio | -0.0080 |
| max_drawdown | 0.0378 |
| cagr | -0.0039 |
| net_avg_win | 93.1092 |
| net_avg_loss | -103.9684 |
| avg_hold_time_bars | 4.8889 |
| exposure | 0.0040 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
