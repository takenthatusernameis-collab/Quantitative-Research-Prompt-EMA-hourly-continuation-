# EMA Hourly Continuation — ONT/USDT P55_100

**Symbol:** ONT/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 381 |
| net_profit_factor | 0.6313 |
| net_win_rate | 0.4751 |
| gross_profit_factor | 0.8650 |
| gross_win_rate | 0.4751 |
| sharpe_ratio | -2.5478 |
| sortino_ratio | -0.7091 |
| max_drawdown | 0.5940 |
| cagr | -0.2771 |
| net_avg_win | 52.8852 |
| net_avg_loss | -75.8106 |
| avg_hold_time_bars | 8.7113 |
| exposure | 0.1502 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
