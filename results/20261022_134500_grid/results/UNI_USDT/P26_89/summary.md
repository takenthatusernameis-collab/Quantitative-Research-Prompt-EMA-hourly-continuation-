# EMA Hourly Continuation — UNI/USDT P26_89

**Symbol:** UNI/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 693 |
| net_profit_factor | 0.5625 |
| net_win_rate | 0.4704 |
| gross_profit_factor | 0.8714 |
| gross_win_rate | 0.4719 |
| sharpe_ratio | -4.6497 |
| sortino_ratio | -1.7193 |
| max_drawdown | 0.8794 |
| cagr | -0.5630 |
| net_avg_win | 34.5056 |
| net_avg_loss | -54.4907 |
| avg_hold_time_bars | 9.7460 |
| exposure | 0.3070 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
