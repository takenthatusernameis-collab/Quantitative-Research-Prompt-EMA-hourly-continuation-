# EMA Hourly Continuation — XDC/USDT P8_26

**Symbol:** XDC/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1513 |
| net_profit_factor | 0.2141 |
| net_win_rate | 0.3748 |
| gross_profit_factor | 0.6355 |
| gross_win_rate | 0.4428 |
| sharpe_ratio | -15.0150 |
| sortino_ratio | -8.3510 |
| max_drawdown | 1.0000 |
| cagr | -0.9882 |
| net_avg_win | 4.8048 |
| net_avg_loss | -13.4505 |
| avg_hold_time_bars | 3.8619 |
| exposure | 0.2656 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
