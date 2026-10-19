# EMA Hourly Continuation — RUNE/USDT P8_100

**Symbol:** RUNE/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 532 |
| net_profit_factor | 0.6868 |
| net_win_rate | 0.4944 |
| gross_profit_factor | 1.0117 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -2.8617 |
| sortino_ratio | -0.9297 |
| max_drawdown | 0.6817 |
| cagr | -0.3596 |
| net_avg_win | 56.1479 |
| net_avg_loss | -79.9290 |
| avg_hold_time_bars | 29.4643 |
| exposure | 0.7125 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
