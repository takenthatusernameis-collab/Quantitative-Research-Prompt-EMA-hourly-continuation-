# EMA Hourly Continuation — BOSON/USDT P144_200

**Symbol:** BOSON/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 414 |
| net_profit_factor | 0.5621 |
| net_win_rate | 0.4807 |
| gross_profit_factor | 0.9624 |
| gross_win_rate | 0.4928 |
| sharpe_ratio | -3.4459 |
| sortino_ratio | -0.9781 |
| max_drawdown | 0.7002 |
| cagr | -0.3811 |
| net_avg_win | 45.1642 |
| net_avg_loss | -74.3728 |
| avg_hold_time_bars | 5.3261 |
| exposure | 0.1002 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
