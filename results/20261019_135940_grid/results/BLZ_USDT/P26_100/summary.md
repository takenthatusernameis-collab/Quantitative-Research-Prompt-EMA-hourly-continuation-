# EMA Hourly Continuation — BLZ/USDT P26_100

**Symbol:** BLZ/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 708 |
| net_profit_factor | 0.5688 |
| net_win_rate | 0.4167 |
| gross_profit_factor | 0.8447 |
| gross_win_rate | 0.4266 |
| sharpe_ratio | -5.9899 |
| sortino_ratio | -2.2371 |
| max_drawdown | 0.9356 |
| cagr | -0.6557 |
| net_avg_win | 41.6772 |
| net_avg_loss | -52.3381 |
| avg_hold_time_bars | 11.4746 |
| exposure | 0.3677 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
