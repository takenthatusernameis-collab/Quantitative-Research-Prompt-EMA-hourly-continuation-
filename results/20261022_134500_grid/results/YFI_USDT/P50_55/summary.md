# EMA Hourly Continuation — YFI/USDT P50_55

**Symbol:** YFI/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 959 |
| net_profit_factor | 0.1494 |
| net_win_rate | 0.2982 |
| gross_profit_factor | 0.8783 |
| gross_win_rate | 0.4161 |
| sharpe_ratio | -15.5736 |
| sortino_ratio | -7.3498 |
| max_drawdown | 1.0000 |
| cagr | -0.9819 |
| net_avg_win | 6.1409 |
| net_avg_loss | -17.4679 |
| avg_hold_time_bars | 1.9885 |
| exposure | 0.0863 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
