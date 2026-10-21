# EMA Hourly Continuation — BONK/USDT P8_34

**Symbol:** BONK/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 715 |
| net_profit_factor | 0.8478 |
| net_win_rate | 0.5133 |
| gross_profit_factor | 1.0441 |
| gross_win_rate | 0.5133 |
| sharpe_ratio | -1.3427 |
| sortino_ratio | -0.5162 |
| max_drawdown | 0.5060 |
| cagr | -0.2145 |
| net_avg_win | 68.9983 |
| net_avg_loss | -85.8297 |
| avg_hold_time_bars | 8.2224 |
| exposure | 0.2672 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
