# EMA Hourly Continuation — T/USDT P8_89

**Symbol:** T/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 627 |
| net_profit_factor | 0.6900 |
| net_win_rate | 0.4880 |
| gross_profit_factor | 1.0626 |
| gross_win_rate | 0.5056 |
| sharpe_ratio | -3.3581 |
| sortino_ratio | -1.1844 |
| max_drawdown | 0.7759 |
| cagr | -0.4297 |
| net_avg_win | 55.0928 |
| net_avg_loss | -76.1164 |
| avg_hold_time_bars | 21.1340 |
| exposure | 0.5996 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
