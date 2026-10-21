# EMA Hourly Continuation — OP/USDT P8_144

**Symbol:** OP/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 332 |
| net_profit_factor | 0.8664 |
| net_win_rate | 0.5060 |
| gross_profit_factor | 1.0144 |
| gross_win_rate | 0.5060 |
| sharpe_ratio | -0.7857 |
| sortino_ratio | -0.2049 |
| max_drawdown | 0.2561 |
| cagr | -0.0927 |
| net_avg_win | 83.6902 |
| net_avg_loss | -98.9542 |
| avg_hold_time_bars | 49.9096 |
| exposure | 0.7532 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
