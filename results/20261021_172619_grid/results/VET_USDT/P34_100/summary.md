# EMA Hourly Continuation — VET/USDT P34_100

**Symbol:** VET/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 436 |
| net_profit_factor | 0.7834 |
| net_win_rate | 0.5138 |
| gross_profit_factor | 1.0400 |
| gross_win_rate | 0.5138 |
| sharpe_ratio | -1.5389 |
| sortino_ratio | -0.4616 |
| max_drawdown | 0.4800 |
| cagr | -0.1916 |
| net_avg_win | 66.8004 |
| net_avg_loss | -90.0998 |
| avg_hold_time_bars | 12.3739 |
| exposure | 0.2452 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
