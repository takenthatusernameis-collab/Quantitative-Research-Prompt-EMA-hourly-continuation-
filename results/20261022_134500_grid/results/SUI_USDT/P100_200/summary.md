# EMA Hourly Continuation — SUI/USDT P100_200

**Symbol:** SUI/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 391 |
| net_profit_factor | 0.4932 |
| net_win_rate | 0.4527 |
| gross_profit_factor | 0.7997 |
| gross_win_rate | 0.4629 |
| sharpe_ratio | -4.1733 |
| sortino_ratio | -1.1503 |
| max_drawdown | 0.7805 |
| cagr | -0.4361 |
| net_avg_win | 41.9395 |
| net_avg_loss | -70.3295 |
| avg_hold_time_bars | 8.2506 |
| exposure | 0.1466 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
