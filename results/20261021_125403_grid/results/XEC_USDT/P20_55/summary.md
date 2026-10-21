# EMA Hourly Continuation — XEC/USDT P20_55

**Symbol:** XEC/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 635 |
| net_profit_factor | 0.6955 |
| net_win_rate | 0.4898 |
| gross_profit_factor | 0.9917 |
| gross_win_rate | 0.4898 |
| sharpe_ratio | -3.2025 |
| sortino_ratio | -1.1547 |
| max_drawdown | 0.7552 |
| cagr | -0.4106 |
| net_avg_win | 54.0962 |
| net_avg_loss | -74.6555 |
| avg_hold_time_bars | 8.5528 |
| exposure | 0.2458 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
