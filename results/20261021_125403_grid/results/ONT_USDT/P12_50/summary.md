# EMA Hourly Continuation — ONT/USDT P12_50

**Symbol:** ONT/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 626 |
| net_profit_factor | 0.7731 |
| net_win_rate | 0.4984 |
| gross_profit_factor | 1.0162 |
| gross_win_rate | 0.4984 |
| sharpe_ratio | -2.2704 |
| sortino_ratio | -0.8121 |
| max_drawdown | 0.6698 |
| cagr | -0.3117 |
| net_avg_win | 66.6441 |
| net_avg_loss | -85.6536 |
| avg_hold_time_bars | 10.7220 |
| exposure | 0.3037 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
