# EMA Hourly Continuation — METIS/USDT P100_200

**Symbol:** METIS/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 281 |
| net_profit_factor | 0.6393 |
| net_win_rate | 0.4448 |
| gross_profit_factor | 0.8056 |
| gross_win_rate | 0.4448 |
| sharpe_ratio | -2.3895 |
| sortino_ratio | -0.5679 |
| max_drawdown | 0.4873 |
| cagr | -0.2307 |
| net_avg_win | 68.4094 |
| net_avg_loss | -85.7363 |
| avg_hold_time_bars | 13.6726 |
| exposure | 0.1746 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
