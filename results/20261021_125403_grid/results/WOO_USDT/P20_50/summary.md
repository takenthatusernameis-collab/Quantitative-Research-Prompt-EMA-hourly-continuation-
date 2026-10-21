# EMA Hourly Continuation — WOO/USDT P20_50

**Symbol:** WOO/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 584 |
| net_profit_factor | 0.6896 |
| net_win_rate | 0.4640 |
| gross_profit_factor | 0.9044 |
| gross_win_rate | 0.4640 |
| sharpe_ratio | -3.2730 |
| sortino_ratio | -1.1271 |
| max_drawdown | 0.7494 |
| cagr | -0.4044 |
| net_avg_win | 59.6742 |
| net_avg_loss | -74.9191 |
| avg_hold_time_bars | 7.7003 |
| exposure | 0.2044 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
