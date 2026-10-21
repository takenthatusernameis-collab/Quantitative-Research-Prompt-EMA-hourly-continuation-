# EMA Hourly Continuation — DOGE/USDT P50_144

**Symbol:** DOGE/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 322 |
| net_profit_factor | 0.7456 |
| net_win_rate | 0.4969 |
| gross_profit_factor | 0.9682 |
| gross_win_rate | 0.4969 |
| sharpe_ratio | -1.5526 |
| sortino_ratio | -0.3987 |
| max_drawdown | 0.4114 |
| cagr | -0.1671 |
| net_avg_win | 67.4455 |
| net_avg_loss | -89.3390 |
| avg_hold_time_bars | 18.4472 |
| exposure | 0.2700 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
