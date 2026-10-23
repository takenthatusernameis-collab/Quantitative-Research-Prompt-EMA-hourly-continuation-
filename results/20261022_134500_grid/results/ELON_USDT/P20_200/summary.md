# EMA Hourly Continuation — ELON/USDT P20_200

**Symbol:** ELON/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 485 |
| net_profit_factor | 0.5669 |
| net_win_rate | 0.4309 |
| gross_profit_factor | 0.7760 |
| gross_win_rate | 0.4330 |
| sharpe_ratio | -4.0339 |
| sortino_ratio | -1.2524 |
| max_drawdown | 0.7765 |
| cagr | -0.4441 |
| net_avg_win | 48.3026 |
| net_avg_loss | -64.5161 |
| avg_hold_time_bars | 25.6165 |
| exposure | 0.5647 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
