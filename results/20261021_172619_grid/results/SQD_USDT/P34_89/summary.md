# EMA Hourly Continuation — SQD/USDT P34_89

**Symbol:** SQD/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 411 |
| net_profit_factor | 0.7652 |
| net_win_rate | 0.4769 |
| gross_profit_factor | 0.9249 |
| gross_win_rate | 0.4769 |
| sharpe_ratio | -1.8455 |
| sortino_ratio | -0.5418 |
| max_drawdown | 0.4741 |
| cagr | -0.2214 |
| net_avg_win | 75.6957 |
| net_avg_loss | -90.1857 |
| avg_hold_time_bars | 11.1946 |
| exposure | 0.2163 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
