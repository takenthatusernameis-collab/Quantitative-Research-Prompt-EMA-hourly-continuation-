# EMA Hourly Continuation — CPOOL/USDT P12_26

**Symbol:** CPOOL/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1418 |
| net_profit_factor | 0.5471 |
| net_win_rate | 0.4379 |
| gross_profit_factor | 0.8557 |
| gross_win_rate | 0.4542 |
| sharpe_ratio | -9.0489 |
| sortino_ratio | -4.7580 |
| max_drawdown | 0.9975 |
| cagr | -0.9074 |
| net_avg_win | 19.4063 |
| net_avg_loss | -27.6361 |
| avg_hold_time_bars | 2.9097 |
| exposure | 0.1875 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
