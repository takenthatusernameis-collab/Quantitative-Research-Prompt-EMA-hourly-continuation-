# EMA Hourly Continuation — BLUR/USDT P21_34

**Symbol:** BLUR/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1125 |
| net_profit_factor | 0.3766 |
| net_win_rate | 0.4213 |
| gross_profit_factor | 0.8103 |
| gross_win_rate | 0.4498 |
| sharpe_ratio | -9.8348 |
| sortino_ratio | -4.6689 |
| max_drawdown | 0.9972 |
| cagr | -0.9014 |
| net_avg_win | 12.7087 |
| net_avg_loss | -24.5698 |
| avg_hold_time_bars | 2.7004 |
| exposure | 0.1375 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
