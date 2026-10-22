# EMA Hourly Continuation — ONDO/USDT P26_89

**Symbol:** ONDO/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 723 |
| net_profit_factor | 0.5846 |
| net_win_rate | 0.4537 |
| gross_profit_factor | 0.8793 |
| gross_win_rate | 0.4620 |
| sharpe_ratio | -4.9727 |
| sortino_ratio | -1.8684 |
| max_drawdown | 0.9011 |
| cagr | -0.5981 |
| net_avg_win | 38.5609 |
| net_avg_loss | -54.7705 |
| avg_hold_time_bars | 8.6418 |
| exposure | 0.2840 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
