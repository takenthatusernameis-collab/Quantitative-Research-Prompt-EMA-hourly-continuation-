# EMA Hourly Continuation — FLOW/USDT P50_89

**Symbol:** FLOW/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 692 |
| net_profit_factor | 0.4535 |
| net_win_rate | 0.4422 |
| gross_profit_factor | 0.8661 |
| gross_win_rate | 0.4595 |
| sharpe_ratio | -6.5384 |
| sortino_ratio | -2.4333 |
| max_drawdown | 0.9519 |
| cagr | -0.6972 |
| net_avg_win | 25.7645 |
| net_avg_loss | -45.0416 |
| avg_hold_time_bars | 4.2890 |
| exposure | 0.1349 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
