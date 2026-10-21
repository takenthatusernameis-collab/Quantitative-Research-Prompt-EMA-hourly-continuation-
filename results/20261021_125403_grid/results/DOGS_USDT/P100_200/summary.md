# EMA Hourly Continuation — DOGS/USDT P100_200

**Symbol:** DOGS/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 230 |
| net_profit_factor | 0.9363 |
| net_win_rate | 0.5391 |
| gross_profit_factor | 1.1564 |
| gross_win_rate | 0.5391 |
| sharpe_ratio | -0.2837 |
| sortino_ratio | -0.0672 |
| max_drawdown | 0.1520 |
| cagr | -0.0342 |
| net_avg_win | 85.4954 |
| net_avg_loss | -106.8123 |
| avg_hold_time_bars | 11.6174 |
| exposure | 0.1418 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
