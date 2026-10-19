# EMA Hourly Continuation — XDC/USDT P8_100

**Symbol:** XDC/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 866 |
| net_profit_factor | 0.3865 |
| net_win_rate | 0.4584 |
| gross_profit_factor | 0.8988 |
| gross_win_rate | 0.4885 |
| sharpe_ratio | -6.7085 |
| sortino_ratio | -2.7265 |
| max_drawdown | 0.9717 |
| cagr | -0.7544 |
| net_avg_win | 15.4001 |
| net_avg_loss | -33.7306 |
| avg_hold_time_bars | 14.1663 |
| exposure | 0.5576 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
