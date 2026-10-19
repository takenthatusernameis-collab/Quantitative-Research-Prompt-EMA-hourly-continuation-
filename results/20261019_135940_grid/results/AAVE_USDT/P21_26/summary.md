# EMA Hourly Continuation — AAVE/USDT P21_26

**Symbol:** AAVE/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1186 |
| net_profit_factor | 0.1752 |
| net_win_rate | 0.3465 |
| gross_profit_factor | 0.5565 |
| gross_win_rate | 0.3811 |
| sharpe_ratio | -15.3537 |
| sortino_ratio | -7.7651 |
| max_drawdown | 1.0000 |
| cagr | -0.9860 |
| net_avg_win | 5.1697 |
| net_avg_loss | -15.6445 |
| avg_hold_time_bars | 1.9174 |
| exposure | 0.1034 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
