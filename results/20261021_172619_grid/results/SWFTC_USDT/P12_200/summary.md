# EMA Hourly Continuation — SWFTC/USDT P12_200

**Symbol:** SWFTC/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 392 |
| net_profit_factor | 0.7808 |
| net_win_rate | 0.4821 |
| gross_profit_factor | 0.9435 |
| gross_win_rate | 0.4821 |
| sharpe_ratio | -1.6726 |
| sortino_ratio | -0.4715 |
| max_drawdown | 0.4457 |
| cagr | -0.1956 |
| net_avg_win | 79.3528 |
| net_avg_loss | -94.6242 |
| avg_hold_time_bars | 34.4617 |
| exposure | 0.6140 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
