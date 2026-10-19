# EMA Hourly Continuation — PENDLE/USDT P21_89

**Symbol:** PENDLE/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 739 |
| net_profit_factor | 0.6557 |
| net_win_rate | 0.4885 |
| gross_profit_factor | 0.9486 |
| gross_win_rate | 0.4939 |
| sharpe_ratio | -3.4228 |
| sortino_ratio | -1.3154 |
| max_drawdown | 0.7902 |
| cagr | -0.4613 |
| net_avg_win | 41.5967 |
| net_avg_loss | -60.5843 |
| avg_hold_time_bars | 11.2314 |
| exposure | 0.3773 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
