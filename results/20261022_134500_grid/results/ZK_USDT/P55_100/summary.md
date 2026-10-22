# EMA Hourly Continuation — ZK/USDT P55_100

**Symbol:** ZK/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 631 |
| net_profit_factor | 0.5529 |
| net_win_rate | 0.4548 |
| gross_profit_factor | 0.9045 |
| gross_win_rate | 0.4628 |
| sharpe_ratio | -5.2695 |
| sortino_ratio | -1.9283 |
| max_drawdown | 0.8900 |
| cagr | -0.6089 |
| net_avg_win | 38.3003 |
| net_avg_loss | -57.7969 |
| avg_hold_time_bars | 5.4263 |
| exposure | 0.1669 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
