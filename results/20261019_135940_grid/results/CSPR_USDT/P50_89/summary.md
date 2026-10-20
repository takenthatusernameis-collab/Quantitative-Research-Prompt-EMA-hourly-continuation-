# EMA Hourly Continuation — CSPR/USDT P50_89

**Symbol:** CSPR/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 946 |
| net_profit_factor | 0.3534 |
| net_win_rate | 0.3953 |
| gross_profit_factor | 0.7042 |
| gross_win_rate | 0.4017 |
| sharpe_ratio | -9.3861 |
| sortino_ratio | -4.0810 |
| max_drawdown | 0.9942 |
| cagr | -0.8713 |
| net_avg_win | 14.5285 |
| net_avg_loss | -26.8805 |
| avg_hold_time_bars | 3.6934 |
| exposure | 0.1588 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
