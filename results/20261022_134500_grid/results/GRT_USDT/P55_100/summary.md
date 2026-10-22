# EMA Hourly Continuation — GRT/USDT P55_100

**Symbol:** GRT/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 632 |
| net_profit_factor | 0.5078 |
| net_win_rate | 0.4620 |
| gross_profit_factor | 0.8855 |
| gross_win_rate | 0.4747 |
| sharpe_ratio | -5.3282 |
| sortino_ratio | -1.8836 |
| max_drawdown | 0.9054 |
| cagr | -0.6010 |
| net_avg_win | 31.8489 |
| net_avg_loss | -53.8680 |
| avg_hold_time_bars | 4.8402 |
| exposure | 0.1384 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
