# EMA Hourly Continuation — STRK/USDT P12_50

**Symbol:** STRK/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1040 |
| net_profit_factor | 0.5659 |
| net_win_rate | 0.4615 |
| gross_profit_factor | 0.9164 |
| gross_win_rate | 0.4702 |
| sharpe_ratio | -6.0184 |
| sortino_ratio | -2.7419 |
| max_drawdown | 0.9632 |
| cagr | -0.7299 |
| net_avg_win | 26.1448 |
| net_avg_loss | -39.6001 |
| avg_hold_time_bars | 7.4212 |
| exposure | 0.3508 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
