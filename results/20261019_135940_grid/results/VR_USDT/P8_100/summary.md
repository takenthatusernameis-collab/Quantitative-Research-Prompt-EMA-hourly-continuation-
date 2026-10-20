# EMA Hourly Continuation — VR/USDT P8_100

**Symbol:** VR/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 819 |
| net_profit_factor | 0.5530 |
| net_win_rate | 0.4139 |
| gross_profit_factor | 0.8098 |
| gross_win_rate | 0.4188 |
| sharpe_ratio | -7.6662 |
| sortino_ratio | -2.9854 |
| max_drawdown | 0.9842 |
| cagr | -0.8069 |
| net_avg_win | 35.9069 |
| net_avg_loss | -45.8576 |
| avg_hold_time_bars | 16.2918 |
| exposure | 0.6065 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
