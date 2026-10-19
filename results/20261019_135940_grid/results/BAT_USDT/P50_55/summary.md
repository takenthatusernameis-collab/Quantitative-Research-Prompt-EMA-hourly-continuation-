# EMA Hourly Continuation — BAT/USDT P50_55

**Symbol:** BAT/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 783 |
| net_profit_factor | 0.1904 |
| net_win_rate | 0.3614 |
| gross_profit_factor | 0.7524 |
| gross_win_rate | 0.4432 |
| sharpe_ratio | -11.7312 |
| sortino_ratio | -4.8196 |
| max_drawdown | 0.9984 |
| cagr | -0.9222 |
| net_avg_win | 8.2942 |
| net_avg_loss | -24.6616 |
| avg_hold_time_bars | 2.1507 |
| exposure | 0.0765 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
