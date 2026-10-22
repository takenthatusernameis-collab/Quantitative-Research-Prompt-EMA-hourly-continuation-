# EMA Hourly Continuation — PIXEL/USDT P12_50

**Symbol:** PIXEL/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1048 |
| net_profit_factor | 0.5897 |
| net_win_rate | 0.4685 |
| gross_profit_factor | 0.9333 |
| gross_win_rate | 0.4790 |
| sharpe_ratio | -5.4471 |
| sortino_ratio | -2.4680 |
| max_drawdown | 0.9530 |
| cagr | -0.6974 |
| net_avg_win | 27.8316 |
| net_avg_loss | -41.6067 |
| avg_hold_time_bars | 8.0048 |
| exposure | 0.3796 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
