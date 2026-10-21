# EMA Hourly Continuation — DOT/USDT P21_55

**Symbol:** DOT/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 475 |
| net_profit_factor | 0.9156 |
| net_win_rate | 0.5558 |
| gross_profit_factor | 1.2459 |
| gross_win_rate | 0.5558 |
| sharpe_ratio | -0.5823 |
| sortino_ratio | -0.1846 |
| max_drawdown | 0.3517 |
| cagr | -0.0855 |
| net_avg_win | 82.6107 |
| net_avg_loss | -112.8908 |
| avg_hold_time_bars | 8.2947 |
| exposure | 0.1791 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
