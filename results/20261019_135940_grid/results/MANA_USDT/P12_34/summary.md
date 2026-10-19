# EMA Hourly Continuation — MANA/USDT P12_34

**Symbol:** MANA/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1275 |
| net_profit_factor | 0.4257 |
| net_win_rate | 0.4306 |
| gross_profit_factor | 0.8478 |
| gross_win_rate | 0.4471 |
| sharpe_ratio | -10.0446 |
| sortino_ratio | -5.0539 |
| max_drawdown | 0.9983 |
| cagr | -0.9207 |
| net_avg_win | 13.4777 |
| net_avg_loss | -23.9422 |
| avg_hold_time_bars | 4.5529 |
| exposure | 0.2639 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
