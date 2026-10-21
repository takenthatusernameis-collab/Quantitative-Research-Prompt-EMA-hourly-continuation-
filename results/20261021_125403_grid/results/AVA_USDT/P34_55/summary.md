# EMA Hourly Continuation — AVA/USDT P34_55

**Symbol:** AVA/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 318 |
| net_profit_factor | 0.7253 |
| net_win_rate | 0.5126 |
| gross_profit_factor | 1.0384 |
| gross_win_rate | 0.5126 |
| sharpe_ratio | -1.7471 |
| sortino_ratio | -0.4488 |
| max_drawdown | 0.4224 |
| cagr | -0.1855 |
| net_avg_win | 65.2339 |
| net_avg_loss | -94.5771 |
| avg_hold_time_bars | 5.6258 |
| exposure | 0.0813 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
