# EMA Hourly Continuation — CTSI/USDT P20_50

**Symbol:** CTSI/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 631 |
| net_profit_factor | 0.6772 |
| net_win_rate | 0.4580 |
| gross_profit_factor | 0.9276 |
| gross_win_rate | 0.4580 |
| sharpe_ratio | -3.8576 |
| sortino_ratio | -1.3821 |
| max_drawdown | 0.8100 |
| cagr | -0.4701 |
| net_avg_win | 57.8507 |
| net_avg_loss | -72.1902 |
| avg_hold_time_bars | 7.1632 |
| exposure | 0.2055 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
