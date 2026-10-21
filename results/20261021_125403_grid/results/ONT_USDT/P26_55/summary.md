# EMA Hourly Continuation — ONT/USDT P26_55

**Symbol:** ONT/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 448 |
| net_profit_factor | 0.7390 |
| net_win_rate | 0.5067 |
| gross_profit_factor | 1.0358 |
| gross_win_rate | 0.5067 |
| sharpe_ratio | -2.1025 |
| sortino_ratio | -0.6381 |
| max_drawdown | 0.5785 |
| cagr | -0.2539 |
| net_avg_win | 65.1566 |
| net_avg_loss | -90.5609 |
| avg_hold_time_bars | 7.0134 |
| exposure | 0.1422 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
