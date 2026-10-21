# EMA Hourly Continuation — WAVES/USDT P8_200

**Symbol:** WAVES/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 393 |
| net_profit_factor | 0.7164 |
| net_win_rate | 0.4733 |
| gross_profit_factor | 0.8953 |
| gross_win_rate | 0.4733 |
| sharpe_ratio | -2.0763 |
| sortino_ratio | -0.5851 |
| max_drawdown | 0.5133 |
| cagr | -0.2374 |
| net_avg_win | 67.0599 |
| net_avg_loss | -84.1053 |
| avg_hold_time_bars | 40.4478 |
| exposure | 0.7225 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
