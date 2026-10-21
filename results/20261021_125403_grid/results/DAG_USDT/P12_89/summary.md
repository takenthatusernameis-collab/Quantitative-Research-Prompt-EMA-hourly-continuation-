# EMA Hourly Continuation — DAG/USDT P12_89

**Symbol:** DAG/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 495 |
| net_profit_factor | 0.7295 |
| net_win_rate | 0.4687 |
| gross_profit_factor | 0.8582 |
| gross_win_rate | 0.4687 |
| sharpe_ratio | -2.0403 |
| sortino_ratio | -0.6449 |
| max_drawdown | 0.5726 |
| cagr | -0.2576 |
| net_avg_win | 61.2270 |
| net_avg_loss | -74.0397 |
| avg_hold_time_bars | 18.6687 |
| exposure | 0.4200 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
