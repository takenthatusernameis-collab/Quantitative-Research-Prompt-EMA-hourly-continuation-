# EMA Hourly Continuation — CWEB/USDT P8_12

**Symbol:** CWEB/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1844 |
| net_profit_factor | 0.1396 |
| net_win_rate | 0.1876 |
| gross_profit_factor | 0.6299 |
| gross_win_rate | 0.2283 |
| sharpe_ratio | -27.3145 |
| sortino_ratio | -18.6677 |
| max_drawdown | 1.0000 |
| cagr | -1.0000 |
| net_avg_win | 4.6879 |
| net_avg_loss | -7.7584 |
| avg_hold_time_bars | 2.5694 |
| exposure | 0.2154 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
