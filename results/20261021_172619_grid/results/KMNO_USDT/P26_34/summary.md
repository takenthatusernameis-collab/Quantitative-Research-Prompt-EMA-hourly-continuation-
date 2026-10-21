# EMA Hourly Continuation — KMNO/USDT P26_34

**Symbol:** KMNO/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 220 |
| net_profit_factor | 0.7064 |
| net_win_rate | 0.5091 |
| gross_profit_factor | 1.0561 |
| gross_win_rate | 0.5136 |
| sharpe_ratio | -1.6451 |
| sortino_ratio | -0.3532 |
| max_drawdown | 0.3497 |
| cagr | -0.1503 |
| net_avg_win | 71.2025 |
| net_avg_loss | -104.5301 |
| avg_hold_time_bars | 5.4227 |
| exposure | 0.0551 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
