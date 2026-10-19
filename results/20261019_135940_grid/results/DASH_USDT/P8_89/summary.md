# EMA Hourly Continuation — DASH/USDT P8_89

**Symbol:** DASH/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 745 |
| net_profit_factor | 0.5433 |
| net_win_rate | 0.4631 |
| gross_profit_factor | 0.9098 |
| gross_win_rate | 0.4698 |
| sharpe_ratio | -4.8431 |
| sortino_ratio | -1.8587 |
| max_drawdown | 0.8961 |
| cagr | -0.5899 |
| net_avg_win | 30.8081 |
| net_avg_loss | -48.9056 |
| avg_hold_time_bars | 19.0349 |
| exposure | 0.6446 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
