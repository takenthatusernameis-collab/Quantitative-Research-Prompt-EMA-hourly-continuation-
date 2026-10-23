# EMA Hourly Continuation — FLOW/USDT P26_55

**Symbol:** FLOW/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 921 |
| net_profit_factor | 0.4467 |
| net_win_rate | 0.4376 |
| gross_profit_factor | 0.8645 |
| gross_win_rate | 0.4549 |
| sharpe_ratio | -7.7803 |
| sortino_ratio | -3.3383 |
| max_drawdown | 0.9844 |
| cagr | -0.8065 |
| net_avg_win | 19.7098 |
| net_avg_loss | -34.3269 |
| avg_hold_time_bars | 4.5364 |
| exposure | 0.1899 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
