# EMA Hourly Continuation — HNT/USDT P20_34

**Symbol:** HNT/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 309 |
| net_profit_factor | 0.5461 |
| net_win_rate | 0.4337 |
| gross_profit_factor | 0.7336 |
| gross_win_rate | 0.4337 |
| sharpe_ratio | -3.0572 |
| sortino_ratio | -0.7633 |
| max_drawdown | 0.5833 |
| cagr | -0.2943 |
| net_avg_win | 52.3859 |
| net_avg_loss | -73.4467 |
| avg_hold_time_bars | 5.3463 |
| exposure | 0.0751 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
