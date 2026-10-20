# EMA Hourly Continuation — AXL/USDT P21_100

**Symbol:** AXL/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 776 |
| net_profit_factor | 0.5803 |
| net_win_rate | 0.4278 |
| gross_profit_factor | 0.8299 |
| gross_win_rate | 0.4317 |
| sharpe_ratio | -5.5916 |
| sortino_ratio | -2.1822 |
| max_drawdown | 0.9287 |
| cagr | -0.6483 |
| net_avg_win | 38.6656 |
| net_avg_loss | -49.8207 |
| avg_hold_time_bars | 10.9755 |
| exposure | 0.3854 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
