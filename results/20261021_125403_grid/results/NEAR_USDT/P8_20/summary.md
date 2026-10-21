# EMA Hourly Continuation — NEAR/USDT P8_20

**Symbol:** NEAR/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 432 |
| net_profit_factor | 0.7579 |
| net_win_rate | 0.4954 |
| gross_profit_factor | 1.0039 |
| gross_win_rate | 0.4954 |
| sharpe_ratio | -1.9674 |
| sortino_ratio | -0.5864 |
| max_drawdown | 0.5018 |
| cagr | -0.2361 |
| net_avg_win | 71.9034 |
| net_avg_loss | -93.1302 |
| avg_hold_time_bars | 5.4306 |
| exposure | 0.1066 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
