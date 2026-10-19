# EMA Hourly Continuation — XLM/USDT P34_200

**Symbol:** XLM/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 411 |
| net_profit_factor | 0.5117 |
| net_win_rate | 0.4672 |
| gross_profit_factor | 0.9134 |
| gross_win_rate | 0.4793 |
| sharpe_ratio | -3.8380 |
| sortino_ratio | -1.0722 |
| max_drawdown | 0.7498 |
| cagr | -0.4198 |
| net_avg_win | 40.6695 |
| net_avg_loss | -69.6803 |
| avg_hold_time_bars | 25.8224 |
| exposure | 0.4824 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
