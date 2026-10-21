# EMA Hourly Continuation — KSM/USDT P26_89

**Symbol:** KSM/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 459 |
| net_profit_factor | 0.7412 |
| net_win_rate | 0.4946 |
| gross_profit_factor | 0.9742 |
| gross_win_rate | 0.4946 |
| sharpe_ratio | -2.0715 |
| sortino_ratio | -0.6349 |
| max_drawdown | 0.5550 |
| cagr | -0.2525 |
| net_avg_win | 65.4086 |
| net_avg_loss | -86.3469 |
| avg_hold_time_bars | 14.5381 |
| exposure | 0.3033 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
