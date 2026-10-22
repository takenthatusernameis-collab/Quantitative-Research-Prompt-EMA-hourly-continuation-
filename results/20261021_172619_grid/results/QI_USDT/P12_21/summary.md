# EMA Hourly Continuation — QI/USDT P12_21

**Symbol:** QI/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 549 |
| net_profit_factor | 0.6195 |
| net_win_rate | 0.4918 |
| gross_profit_factor | 0.9617 |
| gross_win_rate | 0.4936 |
| sharpe_ratio | -3.5609 |
| sortino_ratio | -1.1963 |
| max_drawdown | 0.7532 |
| cagr | -0.4221 |
| net_avg_win | 45.1833 |
| net_avg_loss | -70.5824 |
| avg_hold_time_bars | 5.1749 |
| exposure | 0.1286 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
