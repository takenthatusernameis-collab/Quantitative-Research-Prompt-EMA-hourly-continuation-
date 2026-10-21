# EMA Hourly Continuation — CTC/USDT P50_55

**Symbol:** CTC/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 155 |
| net_profit_factor | 0.4599 |
| net_win_rate | 0.4323 |
| gross_profit_factor | 0.7388 |
| gross_win_rate | 0.4323 |
| sharpe_ratio | -2.8235 |
| sortino_ratio | -0.5041 |
| max_drawdown | 0.4500 |
| cagr | -0.2089 |
| net_avg_win | 56.5314 |
| net_avg_loss | -93.5904 |
| avg_hold_time_bars | 6.1548 |
| exposure | 0.0434 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
