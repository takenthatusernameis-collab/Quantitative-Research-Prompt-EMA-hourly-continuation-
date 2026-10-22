# EMA Hourly Continuation — BIGTIME/USDT P89_100

**Symbol:** BIGTIME/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 172 |
| net_profit_factor | 0.6283 |
| net_win_rate | 0.4826 |
| gross_profit_factor | 0.9417 |
| gross_win_rate | 0.4826 |
| sharpe_ratio | -1.9553 |
| sortino_ratio | -0.3667 |
| max_drawdown | 0.3731 |
| cagr | -0.1554 |
| net_avg_win | 70.6320 |
| net_avg_loss | -104.8428 |
| avg_hold_time_bars | 5.1686 |
| exposure | 0.0402 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
