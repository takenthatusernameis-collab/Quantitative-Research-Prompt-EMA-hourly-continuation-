# EMA Hourly Continuation — SKY/USDT P21_50

**Symbol:** SKY/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 792 |
| net_profit_factor | 0.4638 |
| net_win_rate | 0.4508 |
| gross_profit_factor | 0.8762 |
| gross_win_rate | 0.4747 |
| sharpe_ratio | -7.5356 |
| sortino_ratio | -3.3157 |
| max_drawdown | 0.9641 |
| cagr | -0.8030 |
| net_avg_win | 23.3549 |
| net_avg_loss | -41.3295 |
| avg_hold_time_bars | 4.9444 |
| exposure | 0.2184 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
