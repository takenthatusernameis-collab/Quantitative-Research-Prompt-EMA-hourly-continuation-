# EMA Hourly Continuation — NMR/USDT P21_34

**Symbol:** NMR/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 432 |
| net_profit_factor | 0.6750 |
| net_win_rate | 0.4884 |
| gross_profit_factor | 1.0020 |
| gross_win_rate | 0.4907 |
| sharpe_ratio | -2.9424 |
| sortino_ratio | -0.8767 |
| max_drawdown | 0.6519 |
| cagr | -0.3303 |
| net_avg_win | 62.4828 |
| net_avg_loss | -88.3746 |
| avg_hold_time_bars | 5.4213 |
| exposure | 0.1065 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
