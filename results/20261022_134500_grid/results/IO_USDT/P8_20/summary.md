# EMA Hourly Continuation — IO/USDT P8_20

**Symbol:** IO/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1625 |
| net_profit_factor | 0.5243 |
| net_win_rate | 0.4449 |
| gross_profit_factor | 0.8848 |
| gross_win_rate | 0.4548 |
| sharpe_ratio | -10.1239 |
| sortino_ratio | -5.9056 |
| max_drawdown | 0.9990 |
| cagr | -0.9461 |
| net_avg_win | 15.2315 |
| net_avg_loss | -23.2840 |
| avg_hold_time_bars | 2.7526 |
| exposure | 0.2165 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
