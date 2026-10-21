# EMA Hourly Continuation — RUNE/USDT P20_26

**Symbol:** RUNE/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 180 |
| net_profit_factor | 0.5942 |
| net_win_rate | 0.4778 |
| gross_profit_factor | 0.8864 |
| gross_win_rate | 0.4778 |
| sharpe_ratio | -2.0578 |
| sortino_ratio | -0.3955 |
| max_drawdown | 0.3758 |
| cagr | -0.1664 |
| net_avg_win | 62.4427 |
| net_avg_loss | -96.1478 |
| avg_hold_time_bars | 4.4333 |
| exposure | 0.0363 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
