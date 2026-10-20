# EMA Hourly Continuation — QI/USDT P34_144

**Symbol:** QI/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 504 |
| net_profit_factor | 0.5474 |
| net_win_rate | 0.4563 |
| gross_profit_factor | 0.8705 |
| gross_win_rate | 0.4663 |
| sharpe_ratio | -4.0591 |
| sortino_ratio | -1.2733 |
| max_drawdown | 0.7962 |
| cagr | -0.4613 |
| net_avg_win | 41.5392 |
| net_avg_loss | -63.7002 |
| avg_hold_time_bars | 15.8810 |
| exposure | 0.3622 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
