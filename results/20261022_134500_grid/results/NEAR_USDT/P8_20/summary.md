# EMA Hourly Continuation — NEAR/USDT P8_20

**Symbol:** NEAR/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1729 |
| net_profit_factor | 0.4385 |
| net_win_rate | 0.4430 |
| gross_profit_factor | 0.9394 |
| gross_win_rate | 0.4610 |
| sharpe_ratio | -11.2963 |
| sortino_ratio | -6.5979 |
| max_drawdown | 0.9998 |
| cagr | -0.9646 |
| net_avg_win | 10.1944 |
| net_avg_loss | -18.4908 |
| avg_hold_time_bars | 2.6009 |
| exposure | 0.2044 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
