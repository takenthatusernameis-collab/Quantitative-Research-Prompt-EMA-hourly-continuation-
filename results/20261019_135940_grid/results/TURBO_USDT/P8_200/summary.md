# EMA Hourly Continuation — TURBO/USDT P8_200

**Symbol:** TURBO/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 371 |
| net_profit_factor | 0.6033 |
| net_win_rate | 0.4367 |
| gross_profit_factor | 0.8191 |
| gross_win_rate | 0.4447 |
| sharpe_ratio | -3.6839 |
| sortino_ratio | -1.0933 |
| max_drawdown | 0.6789 |
| cagr | -0.4030 |
| net_avg_win | 61.9755 |
| net_avg_loss | -79.6270 |
| avg_hold_time_bars | 37.5310 |
| exposure | 0.7596 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
