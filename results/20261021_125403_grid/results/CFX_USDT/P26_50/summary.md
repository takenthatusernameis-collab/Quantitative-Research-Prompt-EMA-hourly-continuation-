# EMA Hourly Continuation — CFX/USDT P26_50

**Symbol:** CFX/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 379 |
| net_profit_factor | 0.6117 |
| net_win_rate | 0.4538 |
| gross_profit_factor | 0.8280 |
| gross_win_rate | 0.4538 |
| sharpe_ratio | -3.0157 |
| sortino_ratio | -0.8375 |
| max_drawdown | 0.6345 |
| cagr | -0.3194 |
| net_avg_win | 56.7430 |
| net_avg_loss | -77.0773 |
| avg_hold_time_bars | 7.0422 |
| exposure | 0.1213 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
