# EMA Hourly Continuation — ZRO/USDT P21_200

**Symbol:** ZRO/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 358 |
| net_profit_factor | 0.7486 |
| net_win_rate | 0.4888 |
| gross_profit_factor | 0.9506 |
| gross_win_rate | 0.4888 |
| sharpe_ratio | -1.7293 |
| sortino_ratio | -0.4798 |
| max_drawdown | 0.4146 |
| cagr | -0.2024 |
| net_avg_win | 69.7404 |
| net_avg_loss | -89.0895 |
| avg_hold_time_bars | 35.5642 |
| exposure | 0.6232 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
