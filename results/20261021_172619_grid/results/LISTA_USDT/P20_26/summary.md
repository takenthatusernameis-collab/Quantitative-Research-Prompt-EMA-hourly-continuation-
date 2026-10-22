# EMA Hourly Continuation — LISTA/USDT P20_26

**Symbol:** LISTA/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 307 |
| net_profit_factor | 0.6519 |
| net_win_rate | 0.4756 |
| gross_profit_factor | 0.9379 |
| gross_win_rate | 0.4756 |
| sharpe_ratio | -2.6465 |
| sortino_ratio | -0.6876 |
| max_drawdown | 0.5495 |
| cagr | -0.2713 |
| net_avg_win | 66.9883 |
| net_avg_loss | -93.1890 |
| avg_hold_time_bars | 5.4984 |
| exposure | 0.0825 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
