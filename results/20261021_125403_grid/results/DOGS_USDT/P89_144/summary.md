# EMA Hourly Continuation — DOGS/USDT P89_144

**Symbol:** DOGS/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 235 |
| net_profit_factor | 0.8550 |
| net_win_rate | 0.5191 |
| gross_profit_factor | 1.0812 |
| gross_win_rate | 0.5191 |
| sharpe_ratio | -0.8375 |
| sortino_ratio | -0.1996 |
| max_drawdown | 0.2780 |
| cagr | -0.0892 |
| net_avg_win | 88.0319 |
| net_avg_loss | -111.1597 |
| avg_hold_time_bars | 7.5362 |
| exposure | 0.0940 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
