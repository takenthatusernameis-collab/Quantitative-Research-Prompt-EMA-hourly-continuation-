# EMA Hourly Continuation — ZRO/USDT P21_100

**Symbol:** ZRO/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 615 |
| net_profit_factor | 0.6747 |
| net_win_rate | 0.4797 |
| gross_profit_factor | 0.9283 |
| gross_win_rate | 0.4846 |
| sharpe_ratio | -3.1027 |
| sortino_ratio | -1.1278 |
| max_drawdown | 0.7160 |
| cagr | -0.4127 |
| net_avg_win | 50.0000 |
| net_avg_loss | -68.3123 |
| avg_hold_time_bars | 13.6374 |
| exposure | 0.4105 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
