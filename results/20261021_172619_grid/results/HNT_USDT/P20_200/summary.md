# EMA Hourly Continuation — HNT/USDT P20_200

**Symbol:** HNT/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 279 |
| net_profit_factor | 0.7914 |
| net_win_rate | 0.4803 |
| gross_profit_factor | 0.9105 |
| gross_win_rate | 0.4803 |
| sharpe_ratio | -1.1551 |
| sortino_ratio | -0.2748 |
| max_drawdown | 0.3050 |
| cagr | -0.1202 |
| net_avg_win | 77.8814 |
| net_avg_loss | -90.9403 |
| avg_hold_time_bars | 52.1505 |
| exposure | 0.6614 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
