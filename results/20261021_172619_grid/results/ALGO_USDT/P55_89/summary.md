# EMA Hourly Continuation — ALGO/USDT P55_89

**Symbol:** ALGO/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 289 |
| net_profit_factor | 0.7261 |
| net_win_rate | 0.5052 |
| gross_profit_factor | 1.0040 |
| gross_win_rate | 0.5052 |
| sharpe_ratio | -1.6314 |
| sortino_ratio | -0.3987 |
| max_drawdown | 0.3793 |
| cagr | -0.1671 |
| net_avg_win | 66.8615 |
| net_avg_loss | -94.0109 |
| avg_hold_time_bars | 6.4983 |
| exposure | 0.0854 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
