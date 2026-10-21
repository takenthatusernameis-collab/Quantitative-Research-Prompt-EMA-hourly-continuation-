# EMA Hourly Continuation — TAIKO/USDT P50_144

**Symbol:** TAIKO/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 289 |
| net_profit_factor | 0.7476 |
| net_win_rate | 0.4913 |
| gross_profit_factor | 0.9530 |
| gross_win_rate | 0.4913 |
| sharpe_ratio | -1.5614 |
| sortino_ratio | -0.3902 |
| max_drawdown | 0.3794 |
| cagr | -0.1641 |
| net_avg_win | 72.3345 |
| net_avg_loss | -93.4634 |
| avg_hold_time_bars | 19.8235 |
| exposure | 0.2752 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
