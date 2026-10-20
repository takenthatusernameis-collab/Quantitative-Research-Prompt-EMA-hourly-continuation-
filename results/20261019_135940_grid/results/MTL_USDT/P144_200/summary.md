# EMA Hourly Continuation — MTL/USDT P144_200

**Symbol:** MTL/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 380 |
| net_profit_factor | 0.3771 |
| net_win_rate | 0.4105 |
| gross_profit_factor | 0.7994 |
| gross_win_rate | 0.4395 |
| sharpe_ratio | -5.7352 |
| sortino_ratio | -1.5822 |
| max_drawdown | 0.8613 |
| cagr | -0.5422 |
| net_avg_win | 33.4001 |
| net_avg_loss | -61.6829 |
| avg_hold_time_bars | 6.1158 |
| exposure | 0.1052 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
