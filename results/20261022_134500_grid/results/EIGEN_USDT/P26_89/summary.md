# EMA Hourly Continuation — EIGEN/USDT P26_89

**Symbol:** EIGEN/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 596 |
| net_profit_factor | 0.6735 |
| net_win_rate | 0.4832 |
| gross_profit_factor | 0.9410 |
| gross_win_rate | 0.4849 |
| sharpe_ratio | -3.5260 |
| sortino_ratio | -1.3472 |
| max_drawdown | 0.7326 |
| cagr | -0.4700 |
| net_avg_win | 52.1496 |
| net_avg_loss | -72.4022 |
| avg_hold_time_bars | 8.7534 |
| exposure | 0.2903 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
