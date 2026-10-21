# EMA Hourly Continuation — ZK/USDT P12_100

**Symbol:** ZK/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 476 |
| net_profit_factor | 0.8515 |
| net_win_rate | 0.5042 |
| gross_profit_factor | 1.0183 |
| gross_win_rate | 0.5063 |
| sharpe_ratio | -1.1544 |
| sortino_ratio | -0.3736 |
| max_drawdown | 0.3769 |
| cagr | -0.1609 |
| net_avg_win | 80.4665 |
| net_avg_loss | -96.1050 |
| avg_hold_time_bars | 24.4181 |
| exposure | 0.5667 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
