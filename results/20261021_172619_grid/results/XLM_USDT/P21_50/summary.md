# EMA Hourly Continuation — XLM/USDT P21_50

**Symbol:** XLM/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 466 |
| net_profit_factor | 0.6378 |
| net_win_rate | 0.4936 |
| gross_profit_factor | 0.9622 |
| gross_win_rate | 0.4936 |
| sharpe_ratio | -2.8083 |
| sortino_ratio | -0.8706 |
| max_drawdown | 0.6410 |
| cagr | -0.3279 |
| net_avg_win | 48.3390 |
| net_avg_loss | -73.8587 |
| avg_hold_time_bars | 7.8219 |
| exposure | 0.1657 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
