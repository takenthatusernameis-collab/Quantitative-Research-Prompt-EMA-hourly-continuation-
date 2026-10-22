# EMA Hourly Continuation — RAY/USDT P21_34

**Symbol:** RAY/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1065 |
| net_profit_factor | 0.4703 |
| net_win_rate | 0.4272 |
| gross_profit_factor | 0.9025 |
| gross_win_rate | 0.4516 |
| sharpe_ratio | -9.0446 |
| sortino_ratio | -4.1725 |
| max_drawdown | 0.9945 |
| cagr | -0.8743 |
| net_avg_win | 19.4048 |
| net_avg_loss | -30.7779 |
| avg_hold_time_bars | 2.7812 |
| exposure | 0.1346 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
