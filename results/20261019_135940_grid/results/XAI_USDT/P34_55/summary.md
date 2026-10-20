# EMA Hourly Continuation — XAI/USDT P34_55

**Symbol:** XAI/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 942 |
| net_profit_factor | 0.5454 |
| net_win_rate | 0.4437 |
| gross_profit_factor | 0.9465 |
| gross_win_rate | 0.4692 |
| sharpe_ratio | -7.4346 |
| sortino_ratio | -3.2286 |
| max_drawdown | 0.9822 |
| cagr | -0.7917 |
| net_avg_win | 28.1451 |
| net_avg_loss | -41.1643 |
| avg_hold_time_bars | 3.5170 |
| exposure | 0.1506 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
