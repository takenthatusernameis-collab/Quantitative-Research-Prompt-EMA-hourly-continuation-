# EMA Hourly Continuation — THETA/USDT P26_100

**Symbol:** THETA/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 425 |
| net_profit_factor | 0.7628 |
| net_win_rate | 0.4894 |
| gross_profit_factor | 0.9490 |
| gross_win_rate | 0.4894 |
| sharpe_ratio | -1.6887 |
| sortino_ratio | -0.4974 |
| max_drawdown | 0.4578 |
| cagr | -0.2047 |
| net_avg_win | 67.6387 |
| net_avg_loss | -84.9894 |
| avg_hold_time_bars | 16.3129 |
| exposure | 0.3151 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
