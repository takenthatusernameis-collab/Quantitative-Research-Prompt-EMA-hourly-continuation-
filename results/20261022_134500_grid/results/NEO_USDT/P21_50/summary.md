# EMA Hourly Continuation — NEO/USDT P21_50

**Symbol:** NEO/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1026 |
| net_profit_factor | 0.3632 |
| net_win_rate | 0.4172 |
| gross_profit_factor | 0.7584 |
| gross_win_rate | 0.4396 |
| sharpe_ratio | -9.2534 |
| sortino_ratio | -4.1845 |
| max_drawdown | 0.9946 |
| cagr | -0.8750 |
| net_avg_win | 13.2561 |
| net_avg_loss | -26.1198 |
| avg_hold_time_bars | 4.5224 |
| exposure | 0.2109 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
