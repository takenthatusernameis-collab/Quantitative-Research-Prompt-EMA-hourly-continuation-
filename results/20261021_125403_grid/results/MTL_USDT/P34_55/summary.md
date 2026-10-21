# EMA Hourly Continuation — MTL/USDT P34_55

**Symbol:** MTL/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 455 |
| net_profit_factor | 0.5103 |
| net_win_rate | 0.4286 |
| gross_profit_factor | 0.8078 |
| gross_win_rate | 0.4308 |
| sharpe_ratio | -4.9838 |
| sortino_ratio | -1.5221 |
| max_drawdown | 0.8421 |
| cagr | -0.5065 |
| net_avg_win | 44.4356 |
| net_avg_loss | -65.3111 |
| avg_hold_time_bars | 8.1824 |
| exposure | 0.1685 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
