# EMA Hourly Continuation — AXL/USDT P20_100

**Symbol:** AXL/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 558 |
| net_profit_factor | 0.6573 |
| net_win_rate | 0.4337 |
| gross_profit_factor | 0.8025 |
| gross_win_rate | 0.4337 |
| sharpe_ratio | -3.5439 |
| sortino_ratio | -1.1810 |
| max_drawdown | 0.7525 |
| cagr | -0.4216 |
| net_avg_win | 59.3341 |
| net_avg_loss | -69.1324 |
| avg_hold_time_bars | 15.4731 |
| exposure | 0.3907 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
