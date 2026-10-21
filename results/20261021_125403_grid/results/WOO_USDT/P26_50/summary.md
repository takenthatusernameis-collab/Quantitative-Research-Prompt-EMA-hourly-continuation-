# EMA Hourly Continuation — WOO/USDT P26_50

**Symbol:** WOO/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 475 |
| net_profit_factor | 0.6664 |
| net_win_rate | 0.4737 |
| gross_profit_factor | 0.9022 |
| gross_win_rate | 0.4737 |
| sharpe_ratio | -2.8701 |
| sortino_ratio | -0.8942 |
| max_drawdown | 0.6729 |
| cagr | -0.3361 |
| net_avg_win | 57.0351 |
| net_avg_loss | -77.0310 |
| avg_hold_time_bars | 6.3516 |
| exposure | 0.1371 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
