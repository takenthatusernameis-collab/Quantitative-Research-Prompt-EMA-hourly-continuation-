# EMA Hourly Continuation — MANTA/USDT P26_100

**Symbol:** MANTA/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 629 |
| net_profit_factor | 0.6519 |
| net_win_rate | 0.4690 |
| gross_profit_factor | 0.9580 |
| gross_win_rate | 0.4769 |
| sharpe_ratio | -3.8664 |
| sortino_ratio | -1.3626 |
| max_drawdown | 0.8112 |
| cagr | -0.4796 |
| net_avg_win | 51.1772 |
| net_avg_loss | -69.3351 |
| avg_hold_time_bars | 12.8362 |
| exposure | 0.3670 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
