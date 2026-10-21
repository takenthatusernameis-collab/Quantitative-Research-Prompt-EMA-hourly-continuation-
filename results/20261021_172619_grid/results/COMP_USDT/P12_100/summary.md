# EMA Hourly Continuation — COMP/USDT P12_100

**Symbol:** COMP/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 485 |
| net_profit_factor | 0.7896 |
| net_win_rate | 0.5093 |
| gross_profit_factor | 1.0101 |
| gross_win_rate | 0.5093 |
| sharpe_ratio | -1.4557 |
| sortino_ratio | -0.4599 |
| max_drawdown | 0.4582 |
| cagr | -0.1915 |
| net_avg_win | 62.8403 |
| net_avg_loss | -82.5976 |
| avg_hold_time_bars | 28.4928 |
| exposure | 0.6281 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
