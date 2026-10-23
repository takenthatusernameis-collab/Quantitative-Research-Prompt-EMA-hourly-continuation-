# EMA Hourly Continuation — SQD/USDT P26_200

**Symbol:** SQD/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 407 |
| net_profit_factor | 0.8222 |
| net_win_rate | 0.5184 |
| gross_profit_factor | 1.0920 |
| gross_win_rate | 0.5233 |
| sharpe_ratio | -1.2240 |
| sortino_ratio | -0.3564 |
| max_drawdown | 0.4257 |
| cagr | -0.1567 |
| net_avg_win | 74.2722 |
| net_avg_loss | -97.2491 |
| avg_hold_time_bars | 28.0590 |
| exposure | 0.5368 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
