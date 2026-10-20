# EMA Hourly Continuation — FIDA/USDT P21_50

**Symbol:** FIDA/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 946 |
| net_profit_factor | 0.4792 |
| net_win_rate | 0.4355 |
| gross_profit_factor | 0.8527 |
| gross_win_rate | 0.4514 |
| sharpe_ratio | -7.1518 |
| sortino_ratio | -3.1019 |
| max_drawdown | 0.9785 |
| cagr | -0.7765 |
| net_avg_win | 21.8252 |
| net_avg_loss | -35.1381 |
| avg_hold_time_bars | 5.8034 |
| exposure | 0.2484 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
