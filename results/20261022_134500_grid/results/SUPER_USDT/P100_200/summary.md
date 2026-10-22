# EMA Hourly Continuation — SUPER/USDT P100_200

**Symbol:** SUPER/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 394 |
| net_profit_factor | 0.5556 |
| net_win_rate | 0.4365 |
| gross_profit_factor | 0.8352 |
| gross_win_rate | 0.4492 |
| sharpe_ratio | -4.0427 |
| sortino_ratio | -1.1243 |
| max_drawdown | 0.7612 |
| cagr | -0.4232 |
| net_avg_win | 54.4332 |
| net_avg_loss | -75.9090 |
| avg_hold_time_bars | 8.2487 |
| exposure | 0.1477 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
