# EMA Hourly Continuation — MTL/USDT P20_100

**Symbol:** MTL/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 557 |
| net_profit_factor | 0.5377 |
| net_win_rate | 0.4399 |
| gross_profit_factor | 0.8451 |
| gross_win_rate | 0.4524 |
| sharpe_ratio | -4.8540 |
| sortino_ratio | -1.6010 |
| max_drawdown | 0.8657 |
| cagr | -0.5428 |
| net_avg_win | 40.8794 |
| net_avg_loss | -59.7019 |
| avg_hold_time_bars | 19.4578 |
| exposure | 0.4905 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
