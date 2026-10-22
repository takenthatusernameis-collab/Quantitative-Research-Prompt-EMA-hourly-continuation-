# EMA Hourly Continuation — MANTA/USDT P50_100

**Symbol:** MANTA/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 383 |
| net_profit_factor | 0.7224 |
| net_win_rate | 0.4830 |
| gross_profit_factor | 0.9419 |
| gross_win_rate | 0.4830 |
| sharpe_ratio | -2.1122 |
| sortino_ratio | -0.5908 |
| max_drawdown | 0.4943 |
| cagr | -0.2377 |
| net_avg_win | 69.5404 |
| net_avg_loss | -89.9381 |
| avg_hold_time_bars | 10.0287 |
| exposure | 0.1746 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
