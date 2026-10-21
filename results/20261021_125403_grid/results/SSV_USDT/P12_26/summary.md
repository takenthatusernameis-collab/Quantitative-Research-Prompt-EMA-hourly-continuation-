# EMA Hourly Continuation — SSV/USDT P12_26

**Symbol:** SSV/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 568 |
| net_profit_factor | 0.7391 |
| net_win_rate | 0.4894 |
| gross_profit_factor | 0.9943 |
| gross_win_rate | 0.4894 |
| sharpe_ratio | -2.5691 |
| sortino_ratio | -0.8751 |
| max_drawdown | 0.6576 |
| cagr | -0.3302 |
| net_avg_win | 64.8287 |
| net_avg_loss | -84.0844 |
| avg_hold_time_bars | 5.5616 |
| exposure | 0.1429 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
