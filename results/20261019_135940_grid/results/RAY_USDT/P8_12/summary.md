# EMA Hourly Continuation — RAY/USDT P8_12

**Symbol:** RAY/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1814 |
| net_profit_factor | 0.2991 |
| net_win_rate | 0.3931 |
| gross_profit_factor | 0.8304 |
| gross_win_rate | 0.4333 |
| sharpe_ratio | -15.6338 |
| sortino_ratio | -9.4836 |
| max_drawdown | 1.0000 |
| cagr | -0.9935 |
| net_avg_win | 5.9856 |
| net_avg_loss | -12.9589 |
| avg_hold_time_bars | 1.8809 |
| exposure | 0.1551 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
