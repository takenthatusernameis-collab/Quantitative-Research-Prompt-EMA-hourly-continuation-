# EMA Hourly Continuation — ENS/USDT P26_55

**Symbol:** ENS/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 457 |
| net_profit_factor | 0.8124 |
| net_win_rate | 0.5208 |
| gross_profit_factor | 1.1082 |
| gross_win_rate | 0.5208 |
| sharpe_ratio | -1.5525 |
| sortino_ratio | -0.4783 |
| max_drawdown | 0.4504 |
| cagr | -0.1976 |
| net_avg_win | 77.2850 |
| net_avg_loss | -103.3820 |
| avg_hold_time_bars | 7.3676 |
| exposure | 0.1530 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
