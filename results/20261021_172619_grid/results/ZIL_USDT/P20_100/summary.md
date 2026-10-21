# EMA Hourly Continuation — ZIL/USDT P20_100

**Symbol:** ZIL/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 461 |
| net_profit_factor | 0.7851 |
| net_win_rate | 0.5011 |
| gross_profit_factor | 1.0145 |
| gross_win_rate | 0.5011 |
| sharpe_ratio | -1.7425 |
| sortino_ratio | -0.5358 |
| max_drawdown | 0.5406 |
| cagr | -0.2192 |
| net_avg_win | 73.1636 |
| net_avg_loss | -93.6005 |
| avg_hold_time_bars | 18.7028 |
| exposure | 0.3919 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
