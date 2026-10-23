# EMA Hourly Continuation — ALPINE/USDT P34_89

**Symbol:** ALPINE/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 687 |
| net_profit_factor | 0.5437 |
| net_win_rate | 0.4541 |
| gross_profit_factor | 0.9142 |
| gross_win_rate | 0.4672 |
| sharpe_ratio | -5.5658 |
| sortino_ratio | -2.0461 |
| max_drawdown | 0.9188 |
| cagr | -0.6304 |
| net_avg_win | 35.0509 |
| net_avg_loss | -53.6388 |
| avg_hold_time_bars | 8.7394 |
| exposure | 0.2729 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
