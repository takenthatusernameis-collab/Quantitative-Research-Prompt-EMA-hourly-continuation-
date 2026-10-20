# EMA Hourly Continuation — BICO/USDT P21_144

**Symbol:** BICO/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 443 |
| net_profit_factor | 0.6581 |
| net_win_rate | 0.4582 |
| gross_profit_factor | 0.8568 |
| gross_win_rate | 0.4605 |
| sharpe_ratio | -2.7913 |
| sortino_ratio | -0.8279 |
| max_drawdown | 0.6476 |
| cagr | -0.3226 |
| net_avg_win | 59.1658 |
| net_avg_loss | -76.0459 |
| avg_hold_time_bars | 27.5734 |
| exposure | 0.5552 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
