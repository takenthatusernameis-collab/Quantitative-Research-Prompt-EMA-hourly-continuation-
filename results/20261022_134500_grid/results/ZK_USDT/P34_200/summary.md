# EMA Hourly Continuation — ZK/USDT P34_200

**Symbol:** ZK/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 373 |
| net_profit_factor | 0.6897 |
| net_win_rate | 0.4745 |
| gross_profit_factor | 0.8983 |
| gross_win_rate | 0.4772 |
| sharpe_ratio | -2.2380 |
| sortino_ratio | -0.6325 |
| max_drawdown | 0.5166 |
| cagr | -0.2582 |
| net_avg_win | 63.1862 |
| net_avg_loss | -82.7294 |
| avg_hold_time_bars | 27.9249 |
| exposure | 0.5078 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
