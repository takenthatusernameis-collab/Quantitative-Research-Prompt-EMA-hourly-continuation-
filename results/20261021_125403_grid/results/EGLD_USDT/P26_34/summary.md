# EMA Hourly Continuation — EGLD/USDT P26_34

**Symbol:** EGLD/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 217 |
| net_profit_factor | 0.7070 |
| net_win_rate | 0.5115 |
| gross_profit_factor | 1.0387 |
| gross_win_rate | 0.5115 |
| sharpe_ratio | -1.5457 |
| sortino_ratio | -0.3283 |
| max_drawdown | 0.3351 |
| cagr | -0.1393 |
| net_avg_win | 68.2322 |
| net_avg_loss | -101.0565 |
| avg_hold_time_bars | 5.1382 |
| exposure | 0.0507 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
