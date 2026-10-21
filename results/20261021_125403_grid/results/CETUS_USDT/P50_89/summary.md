# EMA Hourly Continuation — CETUS/USDT P50_89

**Symbol:** CETUS/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 414 |
| net_profit_factor | 0.6898 |
| net_win_rate | 0.4758 |
| gross_profit_factor | 0.8972 |
| gross_win_rate | 0.4758 |
| sharpe_ratio | -2.3336 |
| sortino_ratio | -0.6760 |
| max_drawdown | 0.5490 |
| cagr | -0.2674 |
| net_avg_win | 61.3986 |
| net_avg_loss | -80.8012 |
| avg_hold_time_bars | 6.7391 |
| exposure | 0.1263 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
