# EMA Hourly Continuation — ARB/USDT P34_200

**Symbol:** ARB/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 341 |
| net_profit_factor | 0.8181 |
| net_win_rate | 0.5279 |
| gross_profit_factor | 1.1227 |
| gross_win_rate | 0.5279 |
| sharpe_ratio | -1.1912 |
| sortino_ratio | -0.3111 |
| max_drawdown | 0.3776 |
| cagr | -0.1394 |
| net_avg_win | 78.4813 |
| net_avg_loss | -107.2488 |
| avg_hold_time_bars | 35.4047 |
| exposure | 0.5488 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
