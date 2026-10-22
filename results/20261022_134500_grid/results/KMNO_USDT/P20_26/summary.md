# EMA Hourly Continuation — KMNO/USDT P20_26

**Symbol:** KMNO/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1003 |
| net_profit_factor | 0.2789 |
| net_win_rate | 0.3769 |
| gross_profit_factor | 0.7595 |
| gross_win_rate | 0.4257 |
| sharpe_ratio | -12.0663 |
| sortino_ratio | -5.5502 |
| max_drawdown | 0.9992 |
| cagr | -0.9453 |
| net_avg_win | 10.2260 |
| net_avg_loss | -22.1725 |
| avg_hold_time_bars | 2.2642 |
| exposure | 0.1049 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
