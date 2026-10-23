# EMA Hourly Continuation — BRETT/USDT P20_144

**Symbol:** BRETT/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 403 |
| net_profit_factor | 0.7248 |
| net_win_rate | 0.4665 |
| gross_profit_factor | 0.8880 |
| gross_win_rate | 0.4665 |
| sharpe_ratio | -2.2656 |
| sortino_ratio | -0.6609 |
| max_drawdown | 0.5444 |
| cagr | -0.2664 |
| net_avg_win | 72.9305 |
| net_avg_loss | -87.9820 |
| avg_hold_time_bars | 29.8834 |
| exposure | 0.5795 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
