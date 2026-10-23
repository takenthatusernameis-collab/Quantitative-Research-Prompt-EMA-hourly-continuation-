# EMA Hourly Continuation — BIGTIME/USDT P26_100

**Symbol:** BIGTIME/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 599 |
| net_profit_factor | 0.7211 |
| net_win_rate | 0.4958 |
| gross_profit_factor | 1.0432 |
| gross_win_rate | 0.5058 |
| sharpe_ratio | -2.7476 |
| sortino_ratio | -0.9469 |
| max_drawdown | 0.7152 |
| cagr | -0.3621 |
| net_avg_win | 59.0588 |
| net_avg_loss | -80.5422 |
| avg_hold_time_bars | 14.2738 |
| exposure | 0.3869 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
