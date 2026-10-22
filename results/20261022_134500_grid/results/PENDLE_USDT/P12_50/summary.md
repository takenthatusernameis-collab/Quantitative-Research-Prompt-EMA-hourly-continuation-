# EMA Hourly Continuation — PENDLE/USDT P12_50

**Symbol:** PENDLE/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1075 |
| net_profit_factor | 0.5586 |
| net_win_rate | 0.4605 |
| gross_profit_factor | 0.8875 |
| gross_win_rate | 0.4688 |
| sharpe_ratio | -6.0054 |
| sortino_ratio | -2.7663 |
| max_drawdown | 0.9645 |
| cagr | -0.7342 |
| net_avg_win | 24.6468 |
| net_avg_loss | -37.6578 |
| avg_hold_time_bars | 7.1498 |
| exposure | 0.3494 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
