# EMA Hourly Continuation — REQ/USDT P34_50

**Symbol:** REQ/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 389 |
| net_profit_factor | 0.4682 |
| net_win_rate | 0.4370 |
| gross_profit_factor | 0.8414 |
| gross_win_rate | 0.4422 |
| sharpe_ratio | -5.0359 |
| sortino_ratio | -1.4349 |
| max_drawdown | 0.8134 |
| cagr | -0.4857 |
| net_avg_win | 42.0360 |
| net_avg_loss | -69.6945 |
| avg_hold_time_bars | 5.0411 |
| exposure | 0.0891 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
