# EMA Hourly Continuation — ZK/USDT P34_100

**Symbol:** ZK/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 435 |
| net_profit_factor | 0.8031 |
| net_win_rate | 0.4989 |
| gross_profit_factor | 0.9905 |
| gross_win_rate | 0.4989 |
| sharpe_ratio | -1.4549 |
| sortino_ratio | -0.4499 |
| max_drawdown | 0.3978 |
| cagr | -0.1883 |
| net_avg_win | 72.6200 |
| net_avg_loss | -90.0140 |
| avg_hold_time_bars | 12.7241 |
| exposure | 0.2699 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
