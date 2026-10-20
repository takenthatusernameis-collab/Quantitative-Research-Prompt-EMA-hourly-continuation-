# EMA Hourly Continuation — GALA/USDT P12_34

**Symbol:** GALA/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1326 |
| net_profit_factor | 0.4579 |
| net_win_rate | 0.4434 |
| gross_profit_factor | 0.8320 |
| gross_win_rate | 0.4555 |
| sharpe_ratio | -8.8349 |
| sortino_ratio | -4.5416 |
| max_drawdown | 0.9963 |
| cagr | -0.8917 |
| net_avg_win | 14.3085 |
| net_avg_loss | -24.8994 |
| avg_hold_time_bars | 3.6395 |
| exposure | 0.2194 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
