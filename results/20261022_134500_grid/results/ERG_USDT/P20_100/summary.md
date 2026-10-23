# EMA Hourly Continuation — ERG/USDT P20_100

**Symbol:** ERG/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 721 |
| net_profit_factor | 0.4219 |
| net_win_rate | 0.4105 |
| gross_profit_factor | 0.6671 |
| gross_win_rate | 0.4258 |
| sharpe_ratio | -6.5269 |
| sortino_ratio | -2.4476 |
| max_drawdown | 0.9535 |
| cagr | -0.7025 |
| net_avg_win | 23.4803 |
| net_avg_loss | -38.7626 |
| avg_hold_time_bars | 11.9778 |
| exposure | 0.3925 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
