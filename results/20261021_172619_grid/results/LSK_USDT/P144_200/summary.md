# EMA Hourly Continuation — LSK/USDT P144_200

**Symbol:** LSK/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 255 |
| net_profit_factor | 0.7050 |
| net_win_rate | 0.5176 |
| gross_profit_factor | 1.0577 |
| gross_win_rate | 0.5216 |
| sharpe_ratio | -1.6231 |
| sortino_ratio | -0.3734 |
| max_drawdown | 0.3838 |
| cagr | -0.1578 |
| net_avg_win | 63.4327 |
| net_avg_loss | -96.5599 |
| avg_hold_time_bars | 7.9216 |
| exposure | 0.0918 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
