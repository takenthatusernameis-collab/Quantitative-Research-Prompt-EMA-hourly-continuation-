# EMA Hourly Continuation — CARV/USDT P26_55

**Symbol:** CARV/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 407 |
| net_profit_factor | 0.6102 |
| net_win_rate | 0.4644 |
| gross_profit_factor | 0.8593 |
| gross_win_rate | 0.4668 |
| sharpe_ratio | -3.3333 |
| sortino_ratio | -1.0683 |
| max_drawdown | 0.6385 |
| cagr | -0.3863 |
| net_avg_win | 52.0686 |
| net_avg_loss | -73.9743 |
| avg_hold_time_bars | 7.9214 |
| exposure | 0.1814 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
