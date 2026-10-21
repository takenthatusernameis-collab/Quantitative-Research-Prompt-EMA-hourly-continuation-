# EMA Hourly Continuation — BAT/USDT P12_50

**Symbol:** BAT/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 711 |
| net_profit_factor | 0.6850 |
| net_win_rate | 0.4782 |
| gross_profit_factor | 0.9527 |
| gross_win_rate | 0.4782 |
| sharpe_ratio | -3.4459 |
| sortino_ratio | -1.3121 |
| max_drawdown | 0.7841 |
| cagr | -0.4524 |
| net_avg_win | 49.8564 |
| net_avg_loss | -66.7052 |
| avg_hold_time_bars | 10.4599 |
| exposure | 0.3380 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
