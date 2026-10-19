# EMA Hourly Continuation — ZK/USDT P12_50

**Symbol:** ZK/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1031 |
| net_profit_factor | 0.6951 |
| net_win_rate | 0.4782 |
| gross_profit_factor | 1.0506 |
| gross_win_rate | 0.4830 |
| sharpe_ratio | -5.3278 |
| sortino_ratio | -2.4983 |
| max_drawdown | 0.9410 |
| cagr | -0.6965 |
| net_avg_win | 43.3974 |
| net_avg_loss | -57.2150 |
| avg_hold_time_bars | 7.0233 |
| exposure | 0.3530 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
