# EMA Hourly Continuation — ZK/USDT P20_200

**Symbol:** ZK/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 295 |
| net_profit_factor | 0.8842 |
| net_win_rate | 0.5051 |
| gross_profit_factor | 1.0136 |
| gross_win_rate | 0.5051 |
| sharpe_ratio | -0.6212 |
| sortino_ratio | -0.1583 |
| max_drawdown | 0.2435 |
| cagr | -0.0732 |
| net_avg_win | 83.5833 |
| net_avg_loss | -96.4721 |
| avg_hold_time_bars | 45.2508 |
| exposure | 0.6508 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
