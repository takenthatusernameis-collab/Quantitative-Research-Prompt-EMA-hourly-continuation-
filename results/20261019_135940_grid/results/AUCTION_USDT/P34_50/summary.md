# EMA Hourly Continuation — AUCTION/USDT P34_50

**Symbol:** AUCTION/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 878 |
| net_profit_factor | 0.4003 |
| net_win_rate | 0.4191 |
| gross_profit_factor | 0.8506 |
| gross_win_rate | 0.4544 |
| sharpe_ratio | -9.1503 |
| sortino_ratio | -3.8666 |
| max_drawdown | 0.9921 |
| cagr | -0.8529 |
| net_avg_win | 17.9968 |
| net_avg_loss | -32.4378 |
| avg_hold_time_bars | 3.7597 |
| exposure | 0.1494 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
