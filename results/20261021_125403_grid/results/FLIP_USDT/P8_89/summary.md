# EMA Hourly Continuation — FLIP/USDT P8_89

**Symbol:** FLIP/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 411 |
| net_profit_factor | 0.6538 |
| net_win_rate | 0.4574 |
| gross_profit_factor | 0.8655 |
| gross_win_rate | 0.4599 |
| sharpe_ratio | -2.9051 |
| sortino_ratio | -0.8328 |
| max_drawdown | 0.6455 |
| cagr | -0.3209 |
| net_avg_win | 62.4583 |
| net_avg_loss | -80.5321 |
| avg_hold_time_bars | 34.6326 |
| exposure | 0.6470 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
