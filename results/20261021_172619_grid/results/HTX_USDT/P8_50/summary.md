# EMA Hourly Continuation — HTX/USDT P8_50

**Symbol:** HTX/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 672 |
| net_profit_factor | 0.4938 |
| net_win_rate | 0.4167 |
| gross_profit_factor | 0.8086 |
| gross_win_rate | 0.4226 |
| sharpe_ratio | -6.9447 |
| sortino_ratio | -2.5835 |
| max_drawdown | 0.9540 |
| cagr | -0.7051 |
| net_avg_win | 33.2433 |
| net_avg_loss | -48.0829 |
| avg_hold_time_bars | 14.9970 |
| exposure | 0.4561 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
