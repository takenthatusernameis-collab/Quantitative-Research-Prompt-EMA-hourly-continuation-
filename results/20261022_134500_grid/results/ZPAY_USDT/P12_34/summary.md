# EMA Hourly Continuation — ZPAY/USDT P12_34

**Symbol:** ZPAY/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 975 |
| net_profit_factor | 0.4359 |
| net_win_rate | 0.3374 |
| gross_profit_factor | 0.6818 |
| gross_win_rate | 0.3415 |
| sharpe_ratio | -9.4683 |
| sortino_ratio | -4.1325 |
| max_drawdown | 0.9927 |
| cagr | -0.8577 |
| net_avg_win | 23.3148 |
| net_avg_loss | -27.2407 |
| avg_hold_time_bars | 6.7415 |
| exposure | 0.2974 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
