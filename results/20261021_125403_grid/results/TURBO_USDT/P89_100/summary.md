# EMA Hourly Continuation — TURBO/USDT P89_100

**Symbol:** TURBO/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 99 |
| net_profit_factor | 0.7677 |
| net_win_rate | 0.5152 |
| gross_profit_factor | 1.0448 |
| gross_win_rate | 0.5152 |
| sharpe_ratio | -0.8458 |
| sortino_ratio | -0.1328 |
| max_drawdown | 0.1501 |
| cagr | -0.0587 |
| net_avg_win | 77.0854 |
| net_avg_loss | -106.6882 |
| avg_hold_time_bars | 4.0707 |
| exposure | 0.0220 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
