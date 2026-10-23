# EMA Hourly Continuation — FLUX/USDT P50_89

**Symbol:** FLUX/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 723 |
| net_profit_factor | 0.4464 |
| net_win_rate | 0.4509 |
| gross_profit_factor | 0.8326 |
| gross_win_rate | 0.4620 |
| sharpe_ratio | -6.2364 |
| sortino_ratio | -2.3637 |
| max_drawdown | 0.9479 |
| cagr | -0.6875 |
| net_avg_win | 23.4004 |
| net_avg_loss | -43.0473 |
| avg_hold_time_bars | 4.4329 |
| exposure | 0.1457 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
