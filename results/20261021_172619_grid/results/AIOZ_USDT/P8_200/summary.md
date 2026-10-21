# EMA Hourly Continuation — AIOZ/USDT P8_200

**Symbol:** AIOZ/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 372 |
| net_profit_factor | 0.8985 |
| net_win_rate | 0.5108 |
| gross_profit_factor | 1.0397 |
| gross_win_rate | 0.5108 |
| sharpe_ratio | -0.6493 |
| sortino_ratio | -0.1797 |
| max_drawdown | 0.3558 |
| cagr | -0.0832 |
| net_avg_win | 91.3580 |
| net_avg_loss | -106.1440 |
| avg_hold_time_bars | 44.2608 |
| exposure | 0.7484 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
