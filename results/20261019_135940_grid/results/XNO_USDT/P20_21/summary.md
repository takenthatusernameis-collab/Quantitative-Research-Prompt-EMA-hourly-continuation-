# EMA Hourly Continuation — XNO/USDT P20_21

**Symbol:** XNO/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1341 |
| net_profit_factor | 0.1178 |
| net_win_rate | 0.2461 |
| gross_profit_factor | 0.4832 |
| gross_win_rate | 0.3117 |
| sharpe_ratio | -20.4829 |
| sortino_ratio | -11.5385 |
| max_drawdown | 1.0000 |
| cagr | -0.9984 |
| net_avg_win | 4.0473 |
| net_avg_loss | -11.2123 |
| avg_hold_time_bars | 1.6741 |
| exposure | 0.1020 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
