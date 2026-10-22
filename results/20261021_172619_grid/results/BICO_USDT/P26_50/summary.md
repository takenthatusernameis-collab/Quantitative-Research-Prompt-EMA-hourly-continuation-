# EMA Hourly Continuation — BICO/USDT P26_50

**Symbol:** BICO/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 534 |
| net_profit_factor | 0.5629 |
| net_win_rate | 0.4513 |
| gross_profit_factor | 0.7723 |
| gross_win_rate | 0.4513 |
| sharpe_ratio | -3.6742 |
| sortino_ratio | -1.2098 |
| max_drawdown | 0.7634 |
| cagr | -0.4252 |
| net_avg_win | 40.1289 |
| net_avg_loss | -58.6415 |
| avg_hold_time_bars | 6.5655 |
| exposure | 0.1594 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
