# EMA Hourly Continuation — SQD/USDT P12_200

**Symbol:** SQD/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 343 |
| net_profit_factor | 0.8841 |
| net_win_rate | 0.5015 |
| gross_profit_factor | 1.0002 |
| gross_win_rate | 0.5015 |
| sharpe_ratio | -0.6802 |
| sortino_ratio | -0.1834 |
| max_drawdown | 0.3047 |
| cagr | -0.0841 |
| net_avg_win | 85.1647 |
| net_avg_loss | -96.8948 |
| avg_hold_time_bars | 41.6939 |
| exposure | 0.6722 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
