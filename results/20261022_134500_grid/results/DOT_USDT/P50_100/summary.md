# EMA Hourly Continuation — DOT/USDT P50_100

**Symbol:** DOT/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 579 |
| net_profit_factor | 0.5553 |
| net_win_rate | 0.4732 |
| gross_profit_factor | 0.9653 |
| gross_win_rate | 0.4784 |
| sharpe_ratio | -4.7966 |
| sortino_ratio | -1.6372 |
| max_drawdown | 0.8656 |
| cagr | -0.5478 |
| net_avg_win | 39.3552 |
| net_avg_loss | -63.6740 |
| avg_hold_time_bars | 6.1520 |
| exposure | 0.1619 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
