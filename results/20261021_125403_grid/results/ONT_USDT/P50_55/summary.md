# EMA Hourly Continuation — ONT/USDT P50_55

**Symbol:** ONT/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 147 |
| net_profit_factor | 0.6609 |
| net_win_rate | 0.5034 |
| gross_profit_factor | 1.0043 |
| gross_win_rate | 0.5034 |
| sharpe_ratio | -1.5261 |
| sortino_ratio | -0.2657 |
| max_drawdown | 0.2780 |
| cagr | -0.1147 |
| net_avg_win | 69.7081 |
| net_avg_loss | -106.9179 |
| avg_hold_time_bars | 5.5714 |
| exposure | 0.0371 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
