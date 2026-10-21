# EMA Hourly Continuation — SATS/USDT P8_34

**Symbol:** SATS/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 744 |
| net_profit_factor | 0.8121 |
| net_win_rate | 0.5040 |
| gross_profit_factor | 1.0279 |
| gross_win_rate | 0.5040 |
| sharpe_ratio | -1.9406 |
| sortino_ratio | -0.7565 |
| max_drawdown | 0.6049 |
| cagr | -0.2958 |
| net_avg_win | 67.6842 |
| net_avg_loss | -84.6959 |
| avg_hold_time_bars | 9.5040 |
| exposure | 0.3200 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
