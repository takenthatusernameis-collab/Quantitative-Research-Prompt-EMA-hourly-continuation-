# EMA Hourly Continuation — ETC/USDT P34_50

**Symbol:** ETC/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 925 |
| net_profit_factor | 0.2637 |
| net_win_rate | 0.3816 |
| gross_profit_factor | 0.8089 |
| gross_win_rate | 0.4411 |
| sharpe_ratio | -11.6126 |
| sortino_ratio | -5.1304 |
| max_drawdown | 0.9986 |
| cagr | -0.9276 |
| net_avg_win | 10.1293 |
| net_avg_loss | -23.7097 |
| avg_hold_time_bars | 2.5784 |
| exposure | 0.1084 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
