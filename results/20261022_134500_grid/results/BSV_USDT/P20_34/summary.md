# EMA Hourly Continuation — BSV/USDT P20_34

**Symbol:** BSV/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1263 |
| net_profit_factor | 0.2399 |
| net_win_rate | 0.3840 |
| gross_profit_factor | 0.7078 |
| gross_win_rate | 0.4228 |
| sharpe_ratio | -13.5465 |
| sortino_ratio | -6.9175 |
| max_drawdown | 0.9999 |
| cagr | -0.9729 |
| net_avg_win | 6.5076 |
| net_avg_loss | -16.9088 |
| avg_hold_time_bars | 2.7617 |
| exposure | 0.1585 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
