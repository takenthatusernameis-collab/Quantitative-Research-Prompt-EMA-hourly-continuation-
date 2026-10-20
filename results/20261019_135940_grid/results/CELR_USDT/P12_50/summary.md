# EMA Hourly Continuation — CELR/USDT P12_50

**Symbol:** CELR/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1032 |
| net_profit_factor | 0.5391 |
| net_win_rate | 0.4457 |
| gross_profit_factor | 0.8767 |
| gross_win_rate | 0.4545 |
| sharpe_ratio | -6.5355 |
| sortino_ratio | -2.9526 |
| max_drawdown | 0.9721 |
| cagr | -0.7561 |
| net_avg_win | 24.7077 |
| net_avg_loss | -36.8548 |
| avg_hold_time_bars | 7.8178 |
| exposure | 0.3651 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
