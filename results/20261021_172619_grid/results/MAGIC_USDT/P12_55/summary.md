# EMA Hourly Continuation — MAGIC/USDT P12_55

**Symbol:** MAGIC/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 656 |
| net_profit_factor | 0.7796 |
| net_win_rate | 0.4924 |
| gross_profit_factor | 1.0129 |
| gross_win_rate | 0.4924 |
| sharpe_ratio | -2.4754 |
| sortino_ratio | -0.9055 |
| max_drawdown | 0.6893 |
| cagr | -0.3409 |
| net_avg_win | 71.0814 |
| net_avg_loss | -88.4343 |
| avg_hold_time_bars | 13.8613 |
| exposure | 0.4133 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
