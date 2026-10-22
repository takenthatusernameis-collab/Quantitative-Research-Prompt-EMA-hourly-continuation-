# EMA Hourly Continuation — BLZ/USDT P20_26

**Symbol:** BLZ/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1244 |
| net_profit_factor | 0.2376 |
| net_win_rate | 0.3392 |
| gross_profit_factor | 0.7135 |
| gross_win_rate | 0.3907 |
| sharpe_ratio | -14.9332 |
| sortino_ratio | -7.6163 |
| max_drawdown | 1.0000 |
| cagr | -0.9818 |
| net_avg_win | 7.3830 |
| net_avg_loss | -15.9552 |
| avg_hold_time_bars | 2.8867 |
| exposure | 0.1625 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
