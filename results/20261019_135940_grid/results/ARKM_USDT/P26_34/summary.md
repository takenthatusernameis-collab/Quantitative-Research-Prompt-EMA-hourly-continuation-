# EMA Hourly Continuation — ARKM/USDT P26_34

**Symbol:** ARKM/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1098 |
| net_profit_factor | 0.4056 |
| net_win_rate | 0.3871 |
| gross_profit_factor | 0.8616 |
| gross_win_rate | 0.4217 |
| sharpe_ratio | -11.5311 |
| sortino_ratio | -5.4596 |
| max_drawdown | 0.9991 |
| cagr | -0.9386 |
| net_avg_win | 16.0392 |
| net_avg_loss | -24.9742 |
| avg_hold_time_bars | 2.1393 |
| exposure | 0.1068 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
