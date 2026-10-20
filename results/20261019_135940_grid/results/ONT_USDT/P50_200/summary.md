# EMA Hourly Continuation — ONT/USDT P50_200

**Symbol:** ONT/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 421 |
| net_profit_factor | 0.5344 |
| net_win_rate | 0.4418 |
| gross_profit_factor | 0.8115 |
| gross_win_rate | 0.4537 |
| sharpe_ratio | -3.7730 |
| sortino_ratio | -1.0879 |
| max_drawdown | 0.7378 |
| cagr | -0.4044 |
| net_avg_win | 45.0100 |
| net_avg_loss | -66.6635 |
| avg_hold_time_bars | 19.4727 |
| exposure | 0.3710 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
