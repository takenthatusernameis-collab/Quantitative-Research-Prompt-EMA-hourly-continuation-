# EMA Hourly Continuation — NEAR/USDT P12_34

**Symbol:** NEAR/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1321 |
| net_profit_factor | 0.4912 |
| net_win_rate | 0.4474 |
| gross_profit_factor | 0.8790 |
| gross_win_rate | 0.4550 |
| sharpe_ratio | -8.6366 |
| sortino_ratio | -4.3996 |
| max_drawdown | 0.9959 |
| cagr | -0.8873 |
| net_avg_win | 16.2676 |
| net_avg_loss | -26.8117 |
| avg_hold_time_bars | 3.8728 |
| exposure | 0.2325 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
