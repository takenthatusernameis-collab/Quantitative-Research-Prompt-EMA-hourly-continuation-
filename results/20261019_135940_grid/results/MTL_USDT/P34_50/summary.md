# EMA Hourly Continuation — MTL/USDT P34_50

**Symbol:** MTL/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 846 |
| net_profit_factor | 0.3465 |
| net_win_rate | 0.3889 |
| gross_profit_factor | 0.7976 |
| gross_win_rate | 0.4326 |
| sharpe_ratio | -9.8881 |
| sortino_ratio | -4.1070 |
| max_drawdown | 0.9949 |
| cagr | -0.8747 |
| net_avg_win | 16.0340 |
| net_avg_loss | -29.4431 |
| avg_hold_time_bars | 4.8783 |
| exposure | 0.1868 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
