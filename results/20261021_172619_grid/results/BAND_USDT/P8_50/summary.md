# EMA Hourly Continuation — BAND/USDT P8_50

**Symbol:** BAND/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 747 |
| net_profit_factor | 0.8153 |
| net_win_rate | 0.5141 |
| gross_profit_factor | 1.0680 |
| gross_win_rate | 0.5141 |
| sharpe_ratio | -1.9533 |
| sortino_ratio | -0.7639 |
| max_drawdown | 0.6173 |
| cagr | -0.2978 |
| net_avg_win | 67.8499 |
| net_avg_loss | -88.0327 |
| avg_hold_time_bars | 13.4752 |
| exposure | 0.4555 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
