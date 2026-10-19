# EMA Hourly Continuation — NEAR/USDT P50_55

**Symbol:** NEAR/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 773 |
| net_profit_factor | 0.2122 |
| net_win_rate | 0.3415 |
| gross_profit_factor | 0.5959 |
| gross_win_rate | 0.3777 |
| sharpe_ratio | -12.2375 |
| sortino_ratio | -5.0005 |
| max_drawdown | 0.9990 |
| cagr | -0.9349 |
| net_avg_win | 10.1949 |
| net_avg_loss | -24.9135 |
| avg_hold_time_bars | 1.7361 |
| exposure | 0.0610 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
