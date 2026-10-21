# EMA Hourly Continuation — STRK/USDT P34_100

**Symbol:** STRK/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 391 |
| net_profit_factor | 0.8038 |
| net_win_rate | 0.4987 |
| gross_profit_factor | 0.9888 |
| gross_win_rate | 0.4987 |
| sharpe_ratio | -1.3288 |
| sortino_ratio | -0.3763 |
| max_drawdown | 0.4172 |
| cagr | -0.1599 |
| net_avg_win | 74.4880 |
| net_avg_loss | -92.1935 |
| avg_hold_time_bars | 13.6496 |
| exposure | 0.2426 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
