# EMA Hourly Continuation — DODO/USDT P50_100

**Symbol:** DODO/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 703 |
| net_profit_factor | 0.4749 |
| net_win_rate | 0.4253 |
| gross_profit_factor | 0.7997 |
| gross_win_rate | 0.4395 |
| sharpe_ratio | -6.3491 |
| sortino_ratio | -2.3722 |
| max_drawdown | 0.9461 |
| cagr | -0.6804 |
| net_avg_win | 28.5424 |
| net_avg_loss | -44.4841 |
| avg_hold_time_bars | 5.9303 |
| exposure | 0.1887 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
