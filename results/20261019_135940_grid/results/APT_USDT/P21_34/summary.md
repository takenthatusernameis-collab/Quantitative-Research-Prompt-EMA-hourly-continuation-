# EMA Hourly Continuation — APT/USDT P21_34

**Symbol:** APT/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1158 |
| net_profit_factor | 0.2744 |
| net_win_rate | 0.4033 |
| gross_profit_factor | 0.7204 |
| gross_win_rate | 0.4231 |
| sharpe_ratio | -11.7697 |
| sortino_ratio | -5.6952 |
| max_drawdown | 0.9995 |
| cagr | -0.9493 |
| net_avg_win | 8.0933 |
| net_avg_loss | -19.9334 |
| avg_hold_time_bars | 2.5138 |
| exposure | 0.1323 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
