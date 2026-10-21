# EMA Hourly Continuation — ZK/USDT P26_200

**Symbol:** ZK/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 303 |
| net_profit_factor | 0.8901 |
| net_win_rate | 0.5116 |
| gross_profit_factor | 1.0378 |
| gross_win_rate | 0.5116 |
| sharpe_ratio | -0.5770 |
| sortino_ratio | -0.1493 |
| max_drawdown | 0.1922 |
| cagr | -0.0695 |
| net_avg_win | 81.1494 |
| net_avg_loss | -95.4792 |
| avg_hold_time_bars | 38.1155 |
| exposure | 0.5631 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
