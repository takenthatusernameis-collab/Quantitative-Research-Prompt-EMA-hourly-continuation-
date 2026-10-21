# EMA Hourly Continuation — LSK/USDT P26_200

**Symbol:** LSK/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 324 |
| net_profit_factor | 0.8233 |
| net_win_rate | 0.5154 |
| gross_profit_factor | 1.0440 |
| gross_win_rate | 0.5154 |
| sharpe_ratio | -1.0475 |
| sortino_ratio | -0.2698 |
| max_drawdown | 0.3763 |
| cagr | -0.1191 |
| net_avg_win | 76.1150 |
| net_avg_loss | -98.3396 |
| avg_hold_time_bars | 37.7654 |
| exposure | 0.5562 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
