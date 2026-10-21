# EMA Hourly Continuation — ADA/USDT P20_50

**Symbol:** ADA/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 465 |
| net_profit_factor | 0.7906 |
| net_win_rate | 0.5183 |
| gross_profit_factor | 1.0766 |
| gross_win_rate | 0.5183 |
| sharpe_ratio | -1.5737 |
| sortino_ratio | -0.4888 |
| max_drawdown | 0.4508 |
| cagr | -0.2011 |
| net_avg_win | 67.5297 |
| net_avg_loss | -91.8987 |
| avg_hold_time_bars | 8.1398 |
| exposure | 0.1720 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
