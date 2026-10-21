# EMA Hourly Continuation — TURBO/USDT P100_200

**Symbol:** TURBO/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 221 |
| net_profit_factor | 1.0216 |
| net_win_rate | 0.5611 |
| gross_profit_factor | 1.2656 |
| gross_win_rate | 0.5611 |
| sharpe_ratio | 0.1606 |
| sortino_ratio | 0.0381 |
| max_drawdown | 0.1413 |
| cagr | 0.0113 |
| net_avg_win | 90.3107 |
| net_avg_loss | -113.0039 |
| avg_hold_time_bars | 12.0995 |
| exposure | 0.1459 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
