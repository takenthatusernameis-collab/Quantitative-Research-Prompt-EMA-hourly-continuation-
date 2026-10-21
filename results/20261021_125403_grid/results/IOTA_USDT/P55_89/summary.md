# EMA Hourly Continuation — IOTA/USDT P55_89

**Symbol:** IOTA/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 352 |
| net_profit_factor | 0.5968 |
| net_win_rate | 0.4489 |
| gross_profit_factor | 0.8275 |
| gross_win_rate | 0.4489 |
| sharpe_ratio | -3.1387 |
| sortino_ratio | -0.8398 |
| max_drawdown | 0.6546 |
| cagr | -0.3204 |
| net_avg_win | 58.1796 |
| net_avg_loss | -79.3905 |
| avg_hold_time_bars | 6.1648 |
| exposure | 0.0986 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
