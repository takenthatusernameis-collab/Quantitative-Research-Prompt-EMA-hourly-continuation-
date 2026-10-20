# EMA Hourly Continuation — ARKM/USDT P100_144

**Symbol:** ARKM/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 544 |
| net_profit_factor | 0.5422 |
| net_win_rate | 0.4632 |
| gross_profit_factor | 0.8542 |
| gross_win_rate | 0.4706 |
| sharpe_ratio | -4.4738 |
| sortino_ratio | -1.4794 |
| max_drawdown | 0.8352 |
| cagr | -0.5056 |
| net_avg_win | 38.9927 |
| net_avg_loss | -62.0587 |
| avg_hold_time_bars | 3.7426 |
| exposure | 0.0925 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
