# EMA Hourly Continuation — POLYX/USDT P21_200

**Symbol:** POLYX/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 315 |
| net_profit_factor | 0.8515 |
| net_win_rate | 0.5111 |
| gross_profit_factor | 1.0276 |
| gross_win_rate | 0.5111 |
| sharpe_ratio | -0.8549 |
| sortino_ratio | -0.2172 |
| max_drawdown | 0.2872 |
| cagr | -0.0973 |
| net_avg_win | 80.7718 |
| net_avg_loss | -99.1695 |
| avg_hold_time_bars | 42.5968 |
| exposure | 0.6099 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
