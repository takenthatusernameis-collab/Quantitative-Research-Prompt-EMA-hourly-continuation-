# EMA Hourly Continuation — COMP/USDT P34_50

**Symbol:** COMP/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 353 |
| net_profit_factor | 0.5751 |
| net_win_rate | 0.4674 |
| gross_profit_factor | 0.8650 |
| gross_win_rate | 0.4674 |
| sharpe_ratio | -3.2248 |
| sortino_ratio | -0.8689 |
| max_drawdown | 0.6576 |
| cagr | -0.3299 |
| net_avg_win | 52.0129 |
| net_avg_loss | -79.3790 |
| avg_hold_time_bars | 4.9830 |
| exposure | 0.0800 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
