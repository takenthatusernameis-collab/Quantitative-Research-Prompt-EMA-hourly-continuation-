# EMA Hourly Continuation — XYO/USDT P20_50

**Symbol:** XYO/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 532 |
| net_profit_factor | 0.6507 |
| net_win_rate | 0.4680 |
| gross_profit_factor | 0.9225 |
| gross_win_rate | 0.4699 |
| sharpe_ratio | -3.4902 |
| sortino_ratio | -1.1485 |
| max_drawdown | 0.7448 |
| cagr | -0.4102 |
| net_avg_win | 55.0592 |
| net_avg_loss | -74.4510 |
| avg_hold_time_bars | 8.4192 |
| exposure | 0.2027 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
