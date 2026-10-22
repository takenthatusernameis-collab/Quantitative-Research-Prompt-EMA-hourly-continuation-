# EMA Hourly Continuation — STX/USDT P12_34

**Symbol:** STX/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1285 |
| net_profit_factor | 0.4726 |
| net_win_rate | 0.4428 |
| gross_profit_factor | 0.8703 |
| gross_win_rate | 0.4529 |
| sharpe_ratio | -8.7652 |
| sortino_ratio | -4.4237 |
| max_drawdown | 0.9959 |
| cagr | -0.8856 |
| net_avg_win | 15.6845 |
| net_avg_loss | -26.3719 |
| avg_hold_time_bars | 4.1658 |
| exposure | 0.2422 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
