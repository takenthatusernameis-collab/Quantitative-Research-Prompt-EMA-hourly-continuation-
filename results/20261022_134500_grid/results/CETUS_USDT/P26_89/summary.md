# EMA Hourly Continuation — CETUS/USDT P26_89

**Symbol:** CETUS/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 700 |
| net_profit_factor | 0.6926 |
| net_win_rate | 0.4800 |
| gross_profit_factor | 0.9724 |
| gross_win_rate | 0.4843 |
| sharpe_ratio | -3.5056 |
| sortino_ratio | -1.3081 |
| max_drawdown | 0.7976 |
| cagr | -0.4616 |
| net_avg_win | 53.0022 |
| net_avg_loss | -70.6362 |
| avg_hold_time_bars | 9.8171 |
| exposure | 0.3110 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
