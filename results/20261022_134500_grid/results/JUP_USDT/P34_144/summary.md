# EMA Hourly Continuation — JUP/USDT P34_144

**Symbol:** JUP/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 558 |
| net_profit_factor | 0.5799 |
| net_win_rate | 0.4606 |
| gross_profit_factor | 0.8405 |
| gross_win_rate | 0.4606 |
| sharpe_ratio | -3.9777 |
| sortino_ratio | -1.3165 |
| max_drawdown | 0.8042 |
| cagr | -0.4706 |
| net_avg_win | 42.8412 |
| net_avg_loss | -63.0759 |
| avg_hold_time_bars | 13.3513 |
| exposure | 0.3386 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
