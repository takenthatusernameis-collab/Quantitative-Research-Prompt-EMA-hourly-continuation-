# EMA Hourly Continuation — CHR/USDT P26_100

**Symbol:** CHR/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 674 |
| net_profit_factor | 0.6132 |
| net_win_rate | 0.4555 |
| gross_profit_factor | 0.8750 |
| gross_win_rate | 0.4614 |
| sharpe_ratio | -4.1737 |
| sortino_ratio | -1.5303 |
| max_drawdown | 0.8406 |
| cagr | -0.5119 |
| net_avg_win | 43.1821 |
| net_avg_loss | -58.9080 |
| avg_hold_time_bars | 11.6039 |
| exposure | 0.3539 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
