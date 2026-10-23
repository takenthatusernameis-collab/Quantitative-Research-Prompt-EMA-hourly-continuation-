# EMA Hourly Continuation — NMR/USDT P8_26

**Symbol:** NMR/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1585 |
| net_profit_factor | 0.4534 |
| net_win_rate | 0.4290 |
| gross_profit_factor | 0.9255 |
| gross_win_rate | 0.4599 |
| sharpe_ratio | -10.9983 |
| sortino_ratio | -6.1646 |
| max_drawdown | 0.9996 |
| cagr | -0.9547 |
| net_avg_win | 12.1913 |
| net_avg_loss | -20.2054 |
| avg_hold_time_bars | 3.7666 |
| exposure | 0.2714 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
