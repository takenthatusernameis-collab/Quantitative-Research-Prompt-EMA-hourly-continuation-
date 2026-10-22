# EMA Hourly Continuation — DOGS/USDT P8_200

**Symbol:** DOGS/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 257 |
| net_profit_factor | 0.8303 |
| net_win_rate | 0.4942 |
| gross_profit_factor | 0.9799 |
| gross_win_rate | 0.4942 |
| sharpe_ratio | -1.0140 |
| sortino_ratio | -0.2508 |
| max_drawdown | 0.3190 |
| cagr | -0.1107 |
| net_avg_win | 85.9262 |
| net_avg_loss | -101.1010 |
| avg_hold_time_bars | 56.6498 |
| exposure | 0.7724 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
