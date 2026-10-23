# EMA Hourly Continuation — AVA/USDT P34_50

**Symbol:** AVA/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 881 |
| net_profit_factor | 0.3205 |
| net_win_rate | 0.4245 |
| gross_profit_factor | 0.7749 |
| gross_win_rate | 0.4529 |
| sharpe_ratio | -9.2318 |
| sortino_ratio | -3.8972 |
| max_drawdown | 0.9935 |
| cagr | -0.8630 |
| net_avg_win | 12.5253 |
| net_avg_loss | -28.8294 |
| avg_hold_time_bars | 2.7877 |
| exposure | 0.1116 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
