# EMA Hourly Continuation — BRETT/USDT P34_55

**Symbol:** BRETT/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 292 |
| net_profit_factor | 0.7016 |
| net_win_rate | 0.4760 |
| gross_profit_factor | 0.8894 |
| gross_win_rate | 0.4760 |
| sharpe_ratio | -1.8503 |
| sortino_ratio | -0.4642 |
| max_drawdown | 0.4082 |
| cagr | -0.1925 |
| net_avg_win | 67.2975 |
| net_avg_loss | -87.1413 |
| avg_hold_time_bars | 5.4726 |
| exposure | 0.0769 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
