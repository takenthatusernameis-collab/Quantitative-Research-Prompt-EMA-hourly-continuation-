# EMA Hourly Continuation — HTX/USDT P50_200

**Symbol:** HTX/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 440 |
| net_profit_factor | 0.3503 |
| net_win_rate | 0.3500 |
| gross_profit_factor | 0.7994 |
| gross_win_rate | 0.3886 |
| sharpe_ratio | -8.2472 |
| sortino_ratio | -2.4787 |
| max_drawdown | 0.9651 |
| cagr | -0.7342 |
| net_avg_win | 33.7680 |
| net_avg_loss | -51.9113 |
| avg_hold_time_bars | 21.4068 |
| exposure | 0.4262 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
