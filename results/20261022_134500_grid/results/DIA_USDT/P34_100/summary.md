# EMA Hourly Continuation — DIA/USDT P34_100

**Symbol:** DIA/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 642 |
| net_profit_factor | 0.6228 |
| net_win_rate | 0.4704 |
| gross_profit_factor | 0.9488 |
| gross_win_rate | 0.4813 |
| sharpe_ratio | -4.0983 |
| sortino_ratio | -1.4643 |
| max_drawdown | 0.8397 |
| cagr | -0.4990 |
| net_avg_win | 45.1097 |
| net_avg_loss | -64.3348 |
| avg_hold_time_bars | 9.9190 |
| exposure | 0.2882 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
