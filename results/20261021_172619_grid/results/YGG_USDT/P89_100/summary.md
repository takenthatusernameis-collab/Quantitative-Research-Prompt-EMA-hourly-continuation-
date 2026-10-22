# EMA Hourly Continuation — YGG/USDT P89_100

**Symbol:** YGG/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 134 |
| net_profit_factor | 0.6097 |
| net_win_rate | 0.4627 |
| gross_profit_factor | 0.8616 |
| gross_win_rate | 0.4627 |
| sharpe_ratio | -1.7904 |
| sortino_ratio | -0.2958 |
| max_drawdown | 0.3038 |
| cagr | -0.1274 |
| net_avg_win | 73.2993 |
| net_avg_loss | -103.5231 |
| avg_hold_time_bars | 5.5448 |
| exposure | 0.0336 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
