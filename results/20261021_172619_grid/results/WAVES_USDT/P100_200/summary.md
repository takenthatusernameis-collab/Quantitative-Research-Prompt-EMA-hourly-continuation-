# EMA Hourly Continuation — WAVES/USDT P100_200

**Symbol:** WAVES/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 312 |
| net_profit_factor | 0.6454 |
| net_win_rate | 0.4679 |
| gross_profit_factor | 0.8582 |
| gross_win_rate | 0.4679 |
| sharpe_ratio | -2.3293 |
| sortino_ratio | -0.5864 |
| max_drawdown | 0.5154 |
| cagr | -0.2373 |
| net_avg_win | 61.5370 |
| net_avg_loss | -83.8573 |
| avg_hold_time_bars | 11.0801 |
| exposure | 0.1571 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
