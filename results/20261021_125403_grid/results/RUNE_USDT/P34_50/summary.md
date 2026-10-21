# EMA Hourly Continuation — RUNE/USDT P34_50

**Symbol:** RUNE/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 257 |
| net_profit_factor | 0.6555 |
| net_win_rate | 0.4903 |
| gross_profit_factor | 0.9609 |
| gross_win_rate | 0.4903 |
| sharpe_ratio | -2.1381 |
| sortino_ratio | -0.4921 |
| max_drawdown | 0.4411 |
| cagr | -0.2005 |
| net_avg_win | 64.9198 |
| net_avg_loss | -95.2542 |
| avg_hold_time_bars | 5.3930 |
| exposure | 0.0630 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
