# EMA Hourly Continuation — QNT/USDT P55_144

**Symbol:** QNT/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 599 |
| net_profit_factor | 0.5485 |
| net_win_rate | 0.4691 |
| gross_profit_factor | 0.9194 |
| gross_win_rate | 0.4791 |
| sharpe_ratio | -4.6571 |
| sortino_ratio | -1.6031 |
| max_drawdown | 0.8617 |
| cagr | -0.5380 |
| net_avg_win | 37.0108 |
| net_avg_loss | -59.6286 |
| avg_hold_time_bars | 8.3356 |
| exposure | 0.2270 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
