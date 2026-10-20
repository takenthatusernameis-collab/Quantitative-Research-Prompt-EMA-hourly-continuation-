# EMA Hourly Continuation — POPCAT/USDT P8_34

**Symbol:** POPCAT/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1200 |
| net_profit_factor | 0.6069 |
| net_win_rate | 0.4492 |
| gross_profit_factor | 0.8499 |
| gross_win_rate | 0.4583 |
| sharpe_ratio | -7.0670 |
| sortino_ratio | -3.7079 |
| max_drawdown | 0.9788 |
| cagr | -0.8319 |
| net_avg_win | 28.0334 |
| net_avg_loss | -37.6671 |
| avg_hold_time_bars | 5.5967 |
| exposure | 0.3548 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
