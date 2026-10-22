# EMA Hourly Continuation — AERO/USDT P100_200

**Symbol:** AERO/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 328 |
| net_profit_factor | 0.5874 |
| net_win_rate | 0.4604 |
| gross_profit_factor | 0.8661 |
| gross_win_rate | 0.4634 |
| sharpe_ratio | -3.0413 |
| sortino_ratio | -0.7720 |
| max_drawdown | 0.6219 |
| cagr | -0.3134 |
| net_avg_win | 57.6126 |
| net_avg_loss | -83.6682 |
| avg_hold_time_bars | 9.6494 |
| exposure | 0.1439 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
