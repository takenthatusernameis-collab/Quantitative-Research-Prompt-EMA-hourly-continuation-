# EMA Hourly Continuation — METIS/USDT P21_55

**Symbol:** METIS/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 535 |
| net_profit_factor | 0.7478 |
| net_win_rate | 0.4897 |
| gross_profit_factor | 0.9732 |
| gross_win_rate | 0.4897 |
| sharpe_ratio | -2.2632 |
| sortino_ratio | -0.7489 |
| max_drawdown | 0.6308 |
| cagr | -0.2908 |
| net_avg_win | 65.4382 |
| net_avg_loss | -83.9763 |
| avg_hold_time_bars | 7.9495 |
| exposure | 0.1933 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
