# EMA Hourly Continuation — MLK/USDT P34_200

**Symbol:** MLK/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 355 |
| net_profit_factor | 0.5113 |
| net_win_rate | 0.3746 |
| gross_profit_factor | 0.6594 |
| gross_win_rate | 0.3746 |
| sharpe_ratio | -4.4449 |
| sortino_ratio | -1.1735 |
| max_drawdown | 0.7570 |
| cagr | -0.4241 |
| net_avg_win | 59.1070 |
| net_avg_loss | -69.2601 |
| avg_hold_time_bars | 26.4282 |
| exposure | 0.4246 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
