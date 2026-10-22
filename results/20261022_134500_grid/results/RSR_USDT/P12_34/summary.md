# EMA Hourly Continuation — RSR/USDT P12_34

**Symbol:** RSR/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1268 |
| net_profit_factor | 0.5564 |
| net_win_rate | 0.4574 |
| gross_profit_factor | 0.9465 |
| gross_win_rate | 0.4653 |
| sharpe_ratio | -7.4944 |
| sortino_ratio | -3.7554 |
| max_drawdown | 0.9902 |
| cagr | -0.8393 |
| net_avg_win | 21.4090 |
| net_avg_loss | -32.4359 |
| avg_hold_time_bars | 4.1751 |
| exposure | 0.2406 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
