# EMA Hourly Continuation — KSM/USDT P8_89

**Symbol:** KSM/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 509 |
| net_profit_factor | 0.7235 |
| net_win_rate | 0.4676 |
| gross_profit_factor | 0.8980 |
| gross_win_rate | 0.4676 |
| sharpe_ratio | -2.5297 |
| sortino_ratio | -0.8108 |
| max_drawdown | 0.6254 |
| cagr | -0.3118 |
| net_avg_win | 66.9287 |
| net_avg_loss | -81.2394 |
| avg_hold_time_bars | 28.1690 |
| exposure | 0.6517 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
