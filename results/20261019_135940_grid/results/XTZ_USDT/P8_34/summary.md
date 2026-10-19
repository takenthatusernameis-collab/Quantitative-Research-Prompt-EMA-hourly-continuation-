# EMA Hourly Continuation — XTZ/USDT P8_34

**Symbol:** XTZ/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1412 |
| net_profit_factor | 0.4413 |
| net_win_rate | 0.4582 |
| gross_profit_factor | 0.9299 |
| gross_win_rate | 0.4837 |
| sharpe_ratio | -9.1587 |
| sortino_ratio | -4.8297 |
| max_drawdown | 0.9977 |
| cagr | -0.9100 |
| net_avg_win | 12.1773 |
| net_avg_loss | -23.3400 |
| avg_hold_time_bars | 5.3931 |
| exposure | 0.3461 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
