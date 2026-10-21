# EMA Hourly Continuation — G/USDT P21_34

**Symbol:** G/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 453 |
| net_profit_factor | 0.5927 |
| net_win_rate | 0.4768 |
| gross_profit_factor | 0.9213 |
| gross_win_rate | 0.4768 |
| sharpe_ratio | -3.8321 |
| sortino_ratio | -1.2609 |
| max_drawdown | 0.7229 |
| cagr | -0.4391 |
| net_avg_win | 48.1658 |
| net_avg_loss | -74.0682 |
| avg_hold_time_bars | 6.6424 |
| exposure | 0.1582 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
