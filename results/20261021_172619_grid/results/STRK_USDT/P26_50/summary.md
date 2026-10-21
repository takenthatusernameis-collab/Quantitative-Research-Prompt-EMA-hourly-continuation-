# EMA Hourly Continuation — STRK/USDT P26_50

**Symbol:** STRK/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 364 |
| net_profit_factor | 0.6813 |
| net_win_rate | 0.4698 |
| gross_profit_factor | 0.8889 |
| gross_win_rate | 0.4698 |
| sharpe_ratio | -2.3466 |
| sortino_ratio | -0.6388 |
| max_drawdown | 0.5251 |
| cagr | -0.2534 |
| net_avg_win | 65.0080 |
| net_avg_loss | -84.5400 |
| avg_hold_time_bars | 6.1868 |
| exposure | 0.1024 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
