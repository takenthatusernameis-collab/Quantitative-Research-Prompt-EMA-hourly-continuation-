# EMA Hourly Continuation — XDC/USDT P8_55

**Symbol:** XDC/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 661 |
| net_profit_factor | 0.6050 |
| net_win_rate | 0.4690 |
| gross_profit_factor | 0.9224 |
| gross_win_rate | 0.4705 |
| sharpe_ratio | -4.1100 |
| sortino_ratio | -1.5081 |
| max_drawdown | 0.8260 |
| cagr | -0.5004 |
| net_avg_win | 40.7526 |
| net_avg_loss | -59.4948 |
| avg_hold_time_bars | 12.5946 |
| exposure | 0.3784 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
