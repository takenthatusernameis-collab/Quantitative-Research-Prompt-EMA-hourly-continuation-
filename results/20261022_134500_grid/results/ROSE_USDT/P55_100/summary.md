# EMA Hourly Continuation — ROSE/USDT P55_100

**Symbol:** ROSE/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 645 |
| net_profit_factor | 0.5726 |
| net_win_rate | 0.4682 |
| gross_profit_factor | 0.9178 |
| gross_win_rate | 0.4760 |
| sharpe_ratio | -4.5730 |
| sortino_ratio | -1.6386 |
| max_drawdown | 0.8668 |
| cagr | -0.5447 |
| net_avg_win | 38.2161 |
| net_avg_loss | -58.7612 |
| avg_hold_time_bars | 4.9690 |
| exposure | 0.1457 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
