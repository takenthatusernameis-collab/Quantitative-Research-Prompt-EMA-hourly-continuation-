# EMA Hourly Continuation — HNT/USDT P89_200

**Symbol:** HNT/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 426 |
| net_profit_factor | 0.5248 |
| net_win_rate | 0.4249 |
| gross_profit_factor | 0.7401 |
| gross_win_rate | 0.4296 |
| sharpe_ratio | -4.0267 |
| sortino_ratio | -1.1664 |
| max_drawdown | 0.7682 |
| cagr | -0.4286 |
| net_avg_win | 46.0560 |
| net_avg_loss | -64.8320 |
| avg_hold_time_bars | 12.1596 |
| exposure | 0.2355 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
