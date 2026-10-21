# EMA Hourly Continuation — OSMO/USDT P12_100

**Symbol:** OSMO/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 501 |
| net_profit_factor | 0.8082 |
| net_win_rate | 0.5010 |
| gross_profit_factor | 1.0165 |
| gross_win_rate | 0.5010 |
| sharpe_ratio | -1.6243 |
| sortino_ratio | -0.5204 |
| max_drawdown | 0.5528 |
| cagr | -0.2142 |
| net_avg_win | 76.2142 |
| net_avg_loss | -94.6816 |
| avg_hold_time_bars | 24.5549 |
| exposure | 0.5592 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
