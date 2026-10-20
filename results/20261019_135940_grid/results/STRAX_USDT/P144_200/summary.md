# EMA Hourly Continuation — STRAX/USDT P144_200

**Symbol:** STRAX/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 490 |
| net_profit_factor | 0.3603 |
| net_win_rate | 0.3735 |
| gross_profit_factor | 0.6761 |
| gross_win_rate | 0.4020 |
| sharpe_ratio | -7.0942 |
| sortino_ratio | -2.2513 |
| max_drawdown | 0.9362 |
| cagr | -0.6637 |
| net_avg_win | 28.7561 |
| net_avg_loss | -47.5707 |
| avg_hold_time_bars | 5.8694 |
| exposure | 0.1315 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
