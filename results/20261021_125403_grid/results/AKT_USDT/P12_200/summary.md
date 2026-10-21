# EMA Hourly Continuation — AKT/USDT P12_200

**Symbol:** AKT/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 315 |
| net_profit_factor | 0.9177 |
| net_win_rate | 0.5175 |
| gross_profit_factor | 1.0632 |
| gross_win_rate | 0.5175 |
| sharpe_ratio | -0.4343 |
| sortino_ratio | -0.1108 |
| max_drawdown | 0.1563 |
| cagr | -0.0536 |
| net_avg_win | 88.3564 |
| net_avg_loss | -103.2511 |
| avg_hold_time_bars | 50.1016 |
| exposure | 0.7174 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
