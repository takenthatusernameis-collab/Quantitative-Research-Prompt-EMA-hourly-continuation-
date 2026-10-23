# EMA Hourly Continuation — CELO/USDT P34_50

**Symbol:** CELO/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 902 |
| net_profit_factor | 0.3967 |
| net_win_rate | 0.4412 |
| gross_profit_factor | 0.8305 |
| gross_win_rate | 0.4667 |
| sharpe_ratio | -8.1361 |
| sortino_ratio | -3.4666 |
| max_drawdown | 0.9871 |
| cagr | -0.8197 |
| net_avg_win | 16.2994 |
| net_avg_loss | -32.4493 |
| avg_hold_time_bars | 3.2783 |
| exposure | 0.1338 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
