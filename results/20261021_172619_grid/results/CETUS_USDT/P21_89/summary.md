# EMA Hourly Continuation — CETUS/USDT P21_89

**Symbol:** CETUS/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 540 |
| net_profit_factor | 0.8243 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0148 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.5824 |
| sortino_ratio | -0.5250 |
| max_drawdown | 0.5075 |
| cagr | -0.2168 |
| net_avg_win | 79.9737 |
| net_avg_loss | -97.0160 |
| avg_hold_time_bars | 14.2667 |
| exposure | 0.3486 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
