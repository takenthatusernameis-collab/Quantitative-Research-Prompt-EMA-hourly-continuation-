# EMA Hourly Continuation — VR/USDT P8_200

**Symbol:** VR/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 583 |
| net_profit_factor | 0.5529 |
| net_win_rate | 0.3602 |
| gross_profit_factor | 0.7984 |
| gross_win_rate | 0.3671 |
| sharpe_ratio | -8.1671 |
| sortino_ratio | -2.7107 |
| max_drawdown | 0.9799 |
| cagr | -0.7853 |
| net_avg_win | 57.6585 |
| net_avg_loss | -58.7088 |
| avg_hold_time_bars | 27.3756 |
| exposure | 0.7255 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
