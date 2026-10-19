# EMA Hourly Continuation — RUNE/USDT P12_20

**Symbol:** RUNE/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1483 |
| net_profit_factor | 0.2642 |
| net_win_rate | 0.3796 |
| gross_profit_factor | 0.6992 |
| gross_win_rate | 0.4255 |
| sharpe_ratio | -14.9437 |
| sortino_ratio | -8.2633 |
| max_drawdown | 1.0000 |
| cagr | -0.9875 |
| net_avg_win | 6.3792 |
| net_avg_loss | -14.7732 |
| avg_hold_time_bars | 2.0378 |
| exposure | 0.1374 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
