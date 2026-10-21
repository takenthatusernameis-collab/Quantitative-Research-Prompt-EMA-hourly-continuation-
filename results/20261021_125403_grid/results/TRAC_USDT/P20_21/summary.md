# EMA Hourly Continuation — TRAC/USDT P20_21

**Symbol:** TRAC/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 188 |
| net_profit_factor | 0.7864 |
| net_win_rate | 0.5160 |
| gross_profit_factor | 1.0959 |
| gross_win_rate | 0.5160 |
| sharpe_ratio | -1.1322 |
| sortino_ratio | -0.2232 |
| max_drawdown | 0.3294 |
| cagr | -0.0978 |
| net_avg_win | 86.4255 |
| net_avg_loss | -117.1505 |
| avg_hold_time_bars | 8.2979 |
| exposure | 0.0709 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
