# EMA Hourly Continuation — XLM/USDT P12_21

**Symbol:** XLM/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 266 |
| net_profit_factor | 0.5788 |
| net_win_rate | 0.4812 |
| gross_profit_factor | 0.9089 |
| gross_win_rate | 0.4812 |
| sharpe_ratio | -2.6037 |
| sortino_ratio | -0.6109 |
| max_drawdown | 0.5120 |
| cagr | -0.2432 |
| net_avg_win | 54.0428 |
| net_avg_loss | -86.6032 |
| avg_hold_time_bars | 5.5564 |
| exposure | 0.0672 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
