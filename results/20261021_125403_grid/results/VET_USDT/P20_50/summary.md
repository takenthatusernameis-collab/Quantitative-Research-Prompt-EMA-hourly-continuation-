# EMA Hourly Continuation — VET/USDT P20_50

**Symbol:** VET/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 512 |
| net_profit_factor | 0.8098 |
| net_win_rate | 0.5293 |
| gross_profit_factor | 1.1298 |
| gross_win_rate | 0.5312 |
| sharpe_ratio | -1.5346 |
| sortino_ratio | -0.5010 |
| max_drawdown | 0.4714 |
| cagr | -0.2059 |
| net_avg_win | 69.0540 |
| net_avg_loss | -95.8881 |
| avg_hold_time_bars | 6.9062 |
| exposure | 0.1607 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
