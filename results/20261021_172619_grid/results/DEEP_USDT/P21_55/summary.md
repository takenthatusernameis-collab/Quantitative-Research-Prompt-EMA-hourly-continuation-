# EMA Hourly Continuation — DEEP/USDT P21_55

**Symbol:** DEEP/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 385 |
| net_profit_factor | 0.8649 |
| net_win_rate | 0.5169 |
| gross_profit_factor | 1.0629 |
| gross_win_rate | 0.5169 |
| sharpe_ratio | -0.9811 |
| sortino_ratio | -0.3089 |
| max_drawdown | 0.2908 |
| cagr | -0.1357 |
| net_avg_win | 81.9127 |
| net_avg_loss | -101.3328 |
| avg_hold_time_bars | 8.9039 |
| exposure | 0.1941 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
