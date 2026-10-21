# EMA Hourly Continuation — ONT/USDT P8_200

**Symbol:** ONT/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 365 |
| net_profit_factor | 0.7430 |
| net_win_rate | 0.4685 |
| gross_profit_factor | 0.8812 |
| gross_win_rate | 0.4685 |
| sharpe_ratio | -1.7695 |
| sortino_ratio | -0.4792 |
| max_drawdown | 0.4524 |
| cagr | -0.1985 |
| net_avg_win | 72.3419 |
| net_avg_loss | -85.8170 |
| avg_hold_time_bars | 45.1918 |
| exposure | 0.7464 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
