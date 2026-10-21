# EMA Hourly Continuation — XTZ/USDT P8_34

**Symbol:** XTZ/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 771 |
| net_profit_factor | 0.6946 |
| net_win_rate | 0.5045 |
| gross_profit_factor | 0.9834 |
| gross_win_rate | 0.5045 |
| sharpe_ratio | -2.9154 |
| sortino_ratio | -1.1634 |
| max_drawdown | 0.7456 |
| cagr | -0.4123 |
| net_avg_win | 43.0877 |
| net_avg_loss | -63.1648 |
| avg_hold_time_bars | 8.6537 |
| exposure | 0.3033 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
