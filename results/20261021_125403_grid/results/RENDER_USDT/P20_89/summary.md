# EMA Hourly Continuation — RENDER/USDT P20_89

**Symbol:** RENDER/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 429 |
| net_profit_factor | 0.8674 |
| net_win_rate | 0.5198 |
| gross_profit_factor | 1.0677 |
| gross_win_rate | 0.5198 |
| sharpe_ratio | -0.9544 |
| sortino_ratio | -0.3062 |
| max_drawdown | 0.3670 |
| cagr | -0.1346 |
| net_avg_win | 78.8051 |
| net_avg_loss | -98.3441 |
| avg_hold_time_bars | 15.0163 |
| exposure | 0.3400 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
