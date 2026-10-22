# EMA Hourly Continuation — AEVO/USDT P50_200

**Symbol:** AEVO/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 298 |
| net_profit_factor | 0.9069 |
| net_win_rate | 0.5235 |
| gross_profit_factor | 1.0956 |
| gross_win_rate | 0.5235 |
| sharpe_ratio | -0.5082 |
| sortino_ratio | -0.1261 |
| max_drawdown | 0.2242 |
| cagr | -0.0594 |
| net_avg_win | 89.4543 |
| net_avg_loss | -108.3606 |
| avg_hold_time_bars | 33.0436 |
| exposure | 0.4456 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
