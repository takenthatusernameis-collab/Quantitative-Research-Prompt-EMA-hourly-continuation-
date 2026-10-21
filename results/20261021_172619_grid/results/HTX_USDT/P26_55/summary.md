# EMA Hourly Continuation — HTX/USDT P26_55

**Symbol:** HTX/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 469 |
| net_profit_factor | 0.3723 |
| net_win_rate | 0.3710 |
| gross_profit_factor | 0.6692 |
| gross_win_rate | 0.3774 |
| sharpe_ratio | -7.3767 |
| sortino_ratio | -2.3218 |
| max_drawdown | 0.9374 |
| cagr | -0.6667 |
| net_avg_win | 31.9535 |
| net_avg_loss | -50.6239 |
| avg_hold_time_bars | 8.7548 |
| exposure | 0.1858 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
