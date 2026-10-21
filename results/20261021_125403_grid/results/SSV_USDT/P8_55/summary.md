# EMA Hourly Continuation — SSV/USDT P8_55

**Symbol:** SSV/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 689 |
| net_profit_factor | 0.7595 |
| net_win_rate | 0.4688 |
| gross_profit_factor | 0.9307 |
| gross_win_rate | 0.4702 |
| sharpe_ratio | -2.7859 |
| sortino_ratio | -1.0378 |
| max_drawdown | 0.7174 |
| cagr | -0.3802 |
| net_avg_win | 68.5125 |
| net_avg_loss | -79.6124 |
| avg_hold_time_bars | 16.2946 |
| exposure | 0.5080 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
