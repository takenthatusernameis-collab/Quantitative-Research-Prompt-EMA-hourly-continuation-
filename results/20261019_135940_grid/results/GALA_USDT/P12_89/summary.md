# EMA Hourly Continuation — GALA/USDT P12_89

**Symbol:** GALA/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 643 |
| net_profit_factor | 0.6134 |
| net_win_rate | 0.4619 |
| gross_profit_factor | 0.8661 |
| gross_win_rate | 0.4635 |
| sharpe_ratio | -3.9977 |
| sortino_ratio | -1.4314 |
| max_drawdown | 0.8279 |
| cagr | -0.4920 |
| net_avg_win | 43.6631 |
| net_avg_loss | -61.1050 |
| avg_hold_time_bars | 20.0124 |
| exposure | 0.5849 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
