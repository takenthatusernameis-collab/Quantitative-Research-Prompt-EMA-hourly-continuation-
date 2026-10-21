# EMA Hourly Continuation — BRETT/USDT P21_200

**Symbol:** BRETT/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 217 |
| net_profit_factor | 0.8755 |
| net_win_rate | 0.4931 |
| gross_profit_factor | 0.9734 |
| gross_win_rate | 0.4931 |
| sharpe_ratio | -0.6111 |
| sortino_ratio | -0.1323 |
| max_drawdown | 0.1642 |
| cagr | -0.0612 |
| net_avg_win | 91.4645 |
| net_avg_loss | -101.6249 |
| avg_hold_time_bars | 64.5806 |
| exposure | 0.6743 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
