# EMA Hourly Continuation — DEXE/USDT P12_50

**Symbol:** DEXE/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1036 |
| net_profit_factor | 0.4191 |
| net_win_rate | 0.4295 |
| gross_profit_factor | 0.7455 |
| gross_win_rate | 0.4411 |
| sharpe_ratio | -7.8671 |
| sortino_ratio | -3.5320 |
| max_drawdown | 0.9884 |
| cagr | -0.8302 |
| net_avg_win | 16.0268 |
| net_avg_loss | -28.7911 |
| avg_hold_time_bars | 9.3098 |
| exposure | 0.4384 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
