# EMA Hourly Continuation — KMNO/USDT P26_50

**Symbol:** KMNO/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 407 |
| net_profit_factor | 0.6955 |
| net_win_rate | 0.4889 |
| gross_profit_factor | 0.9530 |
| gross_win_rate | 0.4889 |
| sharpe_ratio | -2.3274 |
| sortino_ratio | -0.6757 |
| max_drawdown | 0.5431 |
| cagr | -0.2687 |
| net_avg_win | 61.8237 |
| net_avg_loss | -85.0470 |
| avg_hold_time_bars | 6.6462 |
| exposure | 0.1249 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
