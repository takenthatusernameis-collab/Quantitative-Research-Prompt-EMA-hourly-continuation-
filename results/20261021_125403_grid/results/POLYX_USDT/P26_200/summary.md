# EMA Hourly Continuation — POLYX/USDT P26_200

**Symbol:** POLYX/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 329 |
| net_profit_factor | 0.7880 |
| net_win_rate | 0.4924 |
| gross_profit_factor | 0.9633 |
| gross_win_rate | 0.4924 |
| sharpe_ratio | -1.3740 |
| sortino_ratio | -0.3552 |
| max_drawdown | 0.3685 |
| cagr | -0.1523 |
| net_avg_win | 77.9172 |
| net_avg_loss | -95.9236 |
| avg_hold_time_bars | 36.4711 |
| exposure | 0.5454 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
