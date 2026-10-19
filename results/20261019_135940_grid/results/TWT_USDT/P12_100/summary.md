# EMA Hourly Continuation — TWT/USDT P12_100

**Symbol:** TWT/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 749 |
| net_profit_factor | 0.5765 |
| net_win_rate | 0.4887 |
| gross_profit_factor | 0.9433 |
| gross_win_rate | 0.4940 |
| sharpe_ratio | -4.4362 |
| sortino_ratio | -1.7033 |
| max_drawdown | 0.8887 |
| cagr | -0.5633 |
| net_avg_win | 32.5499 |
| net_avg_loss | -53.9548 |
| avg_hold_time_bars | 16.6302 |
| exposure | 0.5662 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
