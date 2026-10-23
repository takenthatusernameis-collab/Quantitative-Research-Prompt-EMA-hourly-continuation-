# EMA Hourly Continuation — XYO/USDT P8_34

**Symbol:** XYO/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1472 |
| net_profit_factor | 0.3775 |
| net_win_rate | 0.3859 |
| gross_profit_factor | 0.7765 |
| gross_win_rate | 0.4076 |
| sharpe_ratio | -12.3045 |
| sortino_ratio | -6.6381 |
| max_drawdown | 0.9998 |
| cagr | -0.9649 |
| net_avg_win | 10.6757 |
| net_avg_loss | -17.7673 |
| avg_hold_time_bars | 5.2160 |
| exposure | 0.3474 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
