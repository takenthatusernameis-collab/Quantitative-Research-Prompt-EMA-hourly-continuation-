# EMA Hourly Continuation — ALEX/USDT P12_100

**Symbol:** ALEX/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 493 |
| net_profit_factor | 0.6478 |
| net_win_rate | 0.4665 |
| gross_profit_factor | 0.9581 |
| gross_win_rate | 0.4726 |
| sharpe_ratio | -3.3641 |
| sortino_ratio | -1.0487 |
| max_drawdown | 0.7412 |
| cagr | -0.3943 |
| net_avg_win | 57.2529 |
| net_avg_loss | -77.2960 |
| avg_hold_time_bars | 28.3976 |
| exposure | 0.6364 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
