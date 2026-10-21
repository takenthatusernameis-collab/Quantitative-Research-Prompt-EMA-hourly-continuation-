# EMA Hourly Continuation — SWFTC/USDT P21_89

**Symbol:** SWFTC/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 432 |
| net_profit_factor | 0.7791 |
| net_win_rate | 0.4954 |
| gross_profit_factor | 0.9746 |
| gross_win_rate | 0.4954 |
| sharpe_ratio | -1.5811 |
| sortino_ratio | -0.4701 |
| max_drawdown | 0.4320 |
| cagr | -0.1948 |
| net_avg_win | 69.1576 |
| net_avg_loss | -87.1406 |
| avg_hold_time_bars | 16.4375 |
| exposure | 0.3228 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
