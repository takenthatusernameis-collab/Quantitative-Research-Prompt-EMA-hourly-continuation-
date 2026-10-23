# EMA Hourly Continuation — XYO/USDT P34_50

**Symbol:** XYO/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1000 |
| net_profit_factor | 0.2909 |
| net_win_rate | 0.3380 |
| gross_profit_factor | 0.7609 |
| gross_win_rate | 0.3720 |
| sharpe_ratio | -13.0648 |
| sortino_ratio | -5.9775 |
| max_drawdown | 0.9996 |
| cagr | -0.9555 |
| net_avg_win | 12.1302 |
| net_avg_loss | -21.2932 |
| avg_hold_time_bars | 3.2700 |
| exposure | 0.1480 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
