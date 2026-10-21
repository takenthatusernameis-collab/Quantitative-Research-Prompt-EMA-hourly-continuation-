# EMA Hourly Continuation — COMP/USDT P12_34

**Symbol:** COMP/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 688 |
| net_profit_factor | 0.6452 |
| net_win_rate | 0.4913 |
| gross_profit_factor | 0.9177 |
| gross_win_rate | 0.4913 |
| sharpe_ratio | -3.3432 |
| sortino_ratio | -1.2584 |
| max_drawdown | 0.7741 |
| cagr | -0.4371 |
| net_avg_win | 41.0840 |
| net_avg_loss | -61.4973 |
| avg_hold_time_bars | 7.5029 |
| exposure | 0.2346 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
