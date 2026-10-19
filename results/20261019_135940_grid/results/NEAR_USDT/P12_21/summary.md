# EMA Hourly Continuation — NEAR/USDT P12_21

**Symbol:** NEAR/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1508 |
| net_profit_factor | 0.3817 |
| net_win_rate | 0.4118 |
| gross_profit_factor | 0.8588 |
| gross_win_rate | 0.4277 |
| sharpe_ratio | -12.8987 |
| sortino_ratio | -7.0917 |
| max_drawdown | 0.9999 |
| cagr | -0.9753 |
| net_avg_win | 9.9396 |
| net_avg_loss | -18.2317 |
| avg_hold_time_bars | 2.1505 |
| exposure | 0.1474 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
