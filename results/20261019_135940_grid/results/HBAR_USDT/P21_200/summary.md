# EMA Hourly Continuation — HBAR/USDT P21_200

**Symbol:** HBAR/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 372 |
| net_profit_factor | 0.6238 |
| net_win_rate | 0.4839 |
| gross_profit_factor | 0.9555 |
| gross_win_rate | 0.4919 |
| sharpe_ratio | -2.8807 |
| sortino_ratio | -0.7683 |
| max_drawdown | 0.6294 |
| cagr | -0.3179 |
| net_avg_win | 56.8781 |
| net_avg_loss | -85.4803 |
| avg_hold_time_bars | 38.5430 |
| exposure | 0.6517 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
