# EMA Hourly Continuation — LUNA/USDT P34_200

**Symbol:** LUNA/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 490 |
| net_profit_factor | 0.5743 |
| net_win_rate | 0.4510 |
| gross_profit_factor | 0.8617 |
| gross_win_rate | 0.4531 |
| sharpe_ratio | -4.0984 |
| sortino_ratio | -1.2779 |
| max_drawdown | 0.7935 |
| cagr | -0.4561 |
| net_avg_win | 47.8074 |
| net_avg_loss | -68.3951 |
| avg_hold_time_bars | 20.9959 |
| exposure | 0.4676 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
