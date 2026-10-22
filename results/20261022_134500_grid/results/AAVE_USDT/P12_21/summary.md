# EMA Hourly Continuation — AAVE/USDT P12_21

**Symbol:** AAVE/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1460 |
| net_profit_factor | 0.2528 |
| net_win_rate | 0.3945 |
| gross_profit_factor | 0.6953 |
| gross_win_rate | 0.4158 |
| sharpe_ratio | -13.8812 |
| sortino_ratio | -7.5490 |
| max_drawdown | 1.0000 |
| cagr | -0.9810 |
| net_avg_win | 5.8728 |
| net_avg_loss | -15.1383 |
| avg_hold_time_bars | 2.3911 |
| exposure | 0.1587 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
