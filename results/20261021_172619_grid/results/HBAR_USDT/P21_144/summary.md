# EMA Hourly Continuation — HBAR/USDT P21_144

**Symbol:** HBAR/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 352 |
| net_profit_factor | 0.8355 |
| net_win_rate | 0.5114 |
| gross_profit_factor | 1.0374 |
| gross_win_rate | 0.5114 |
| sharpe_ratio | -1.0382 |
| sortino_ratio | -0.2797 |
| max_drawdown | 0.3530 |
| cagr | -0.1222 |
| net_avg_win | 78.7919 |
| net_avg_loss | -98.6869 |
| avg_hold_time_bars | 35.8125 |
| exposure | 0.5730 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
